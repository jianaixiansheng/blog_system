from django.db import models
from django.core import validators

# Create your models here.

class UserInfo(models.Model):
    """用户表"""
    user_numbers=models.BigIntegerField(null=True)
    user_password=models.CharField(max_length=20, null=True)
    user_name = models.CharField(max_length=20)
    user_sex = models.CharField(max_length=20)
    user_sign = models.TextField()
    user_birth = models.DateField()
    user_city = models.CharField(max_length=20)
    user_one_level = models.IntegerField()
    user_member_level = models.IntegerField()


class PhotoAlbum(models.Model):
    """用户相册字段"""
    user_image = models.ImageField(upload_to='image')
    image_time = models.DateTimeField(auto_now_add=True)
    image_type = models.CharField(max_length=10)
    user_fk = models.ForeignKey('UserInfo',on_delete=models.CASCADE)


class DynamicStatus(models.Model):
    """用户动态表"""
    #发表动态的时间
    d_time = models.DateTimeField(auto_now_add=True)
    # 发表的动态内容
    d_content = models.TextField()
    # 发表的图片
    d_picture = models.FileField(upload_to='picture', null=True, validators=[validators.FileExtensionValidator('jpg', 'png', 'txt')], max_length=1000)
    # 点赞的数量
    d_num = models.IntegerField(default=0)
    # 喜欢的数量
    d_like = models.IntegerField(default=0)
    # 转发之后附加内容
    new_content = models.TextField(null=True)
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

    #被关注的人
    a_b_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)

class Comment(models.Model):
    """评论表"""
    #评论的内容
    c_content = models.TextField()
    # 被评论的用户
    c_b_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    # 评论的用户
    c_user = models.IntegerField()
    # 被评论的文章
    c_b_dynamic = models.ForeignKey('DynamicStatus',on_delete=models.CASCADE)
    # 被评论的评论的ID
    c_b_commentID = models.ForeignKey('Comment',on_delete=models.CASCADE)

# 访客表


class GuestLog(models.Model):
    g_b_user=models.IntegerField()
    # 被访问的用户
    g_user=models.ForeignKey('UserInfo',on_delete=models.CASCADE)
    # 访问的用户
    g_date=models.DateTimeField(auto_now=True)
