from django.db import models
from django.core import validators


# Create your models here.


class UserInfo(models.Model):
    """用户表"""
    user_numbers = models.BigIntegerField(null=True,verbose_name='账号')
    user_password = models.CharField(max_length=20, null=True,verbose_name='密码')
    user_name = models.CharField(max_length=20,verbose_name='用户名')
    user_sex = models.CharField(default='请修改', max_length=20,verbose_name='性别')
    user_sign = models.TextField(default='空空如也',verbose_name='个性签名')
    user_birth = models.DateField(auto_now_add=True,verbose_name='出生日期')
    user_city = models.CharField(default='请修改',max_length=20,verbose_name='所在地')
    user_one_level = models.IntegerField(default=1,verbose_name='用户等级')
    user_member_level = models.IntegerField(default=1,verbose_name='会员等级')
    user_PORT = models.IntegerField(default=0)
    user_jude = models.IntegerField(default=0)
    user_IP  = models.CharField(max_length=20,null=True,blank=True)

class levelsystem(models.Model):
    userid = models.ForeignKey(to='UserInfo', db_column='user_id', on_delete=models.CASCADE,verbose_name='用户id')
    signnumber = models.IntegerField(db_column='sign_num',verbose_name='登陆天数')
    memberopendata = models.DateField(null=True, db_column='member_open_data',verbose_name='会员充值日期')
    duedata = models.DateField(null=True, db_column='member_due_data',verbose_name='会员到期时间')
    sign = models.DateField(auto_now=True,verbose_name='最后签到日期')
    userimg = models.TextField(verbose_name='用户头像编码')

    class Meta:
        db_table = 'level_system'


# class PhotoAlbum(models.Model):
#     """用户相册字段"""
#     user_image = models.ImageField(upload_to='image',verbose_name='图片地址')
#     image_time = models.DateTimeField(auto_now_add=True,verbose_name='时间')
#     image_type = models.CharField(max_length=10,verbose_name='类型')
#     user_fk = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


class DynamicStatus(models.Model):
    """用户动态表"""
    # 发表动态的时间
    d_time = models.DateTimeField(auto_now_add=True,verbose_name='时间')
    # 发表的动态内容
    d_content = models.TextField(verbose_name='内容')
    # 发表的图片
    d_picture = models.FileField(upload_to='picture', null=True,
                                 validators=[validators.FileExtensionValidator('jpg', 'png', 'txt')], max_length=1000,verbose_name='图片')
    # 点赞的数量
    d_num = models.IntegerField(default=0,verbose_name='点赞数')
    # 喜欢的数量
    # 转发数量
    d_move = models.IntegerField(default=0)
    d_like = models.IntegerField(default=0,verbose_name='喜欢数')
    # 转发之后附加内容
    new_content = models.TextField(null=True,verbose_name='转发')
    # 谁发表的动态
    user_id = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


class Move_text(models.Model):
    # 转发的时间
    d_b_time = models.DateTimeField(auto_now_add=True, null=True)
    # 被转发的用户的ID（也就是这篇文章是谁写的）
    d_user = models.IntegerField(null=True)
    # 转发的用户的ID（也就是谁转发的）
    d_z_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


# 点赞表
class Thumps_up(models.Model):
    # 谁点的赞
    u = models.ForeignKey(UserInfo, on_delete=models.PROTECT)
    # 赞的那个动态
    article = models.ForeignKey(DynamicStatus, on_delete=models.PROTECT)


# 喜欢表
class love(models.Model):
    # 谁喜欢这条动态
    u = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    # 喜欢那条动态
    U_Article = models.ForeignKey(DynamicStatus, on_delete=models.CASCADE)


class AttentionPerson(models.Model):
    """关注的人"""
    # 我====》关注
    a_user = models.IntegerField()

    # 被关注的人
    a_b_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


class Comment(models.Model):
    """评论表"""
    # 评论的内容
    c_content = models.TextField(verbose_name='内容', null=True)
    # 被评论的文章
    c_b_dynamic = models.ForeignKey('DynamicStatus', on_delete=models.CASCADE, null=True)
    # 被评论的评论的ID
    c_b_commentID = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name='parent_comment')
    root = models.ForeignKey('Comment', related_name='root_comment', null=True, on_delete=models.DO_NOTHING)
    # 评论的时间
    comment_time = models.DateTimeField(auto_now_add=True, null=True)
    # 二级评论回复的人
    reply_to = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, null=True, related_name='replies')
    # 评论的用户
    user = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, related_name='comments', null=True)



# 访客表


class GuestLog(models.Model):
    g_b_user=models.IntegerField()
    # 被访问的用户
    g_user=models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    # 访问的用户
    g_date=models.DateTimeField(auto_now=True)

    g_num = models.IntegerField(default=0)
