from django.db import models
# Create your models here.

class PhotoAlbum(models.Model):
    """用户相册字段"""
    user_image = models.ImageField(upload_to='picture',verbose_name='相册地址',blank=True)
    image_type = models.CharField(max_length=10,verbose_name='相册类型')
    user_fk = models.ForeignKey('body.UserInfo', on_delete=models.CASCADE)
    isDelete = models.IntegerField(default=0) # 0代表未删除，1代表删除
    class Meta:
        verbose_name_plural="相册"




class PhotoGraph(models.Model):
    '''用户图片字段'''
    user_image_url = models.ImageField(upload_to="picture",verbose_name="图片地址",blank=True)
    I_A = models.ManyToManyField("PhotoAlbum",verbose_name="所属相册")
    isDelete = models.IntegerField(default=0) # 0代表未删除，1代表删除

    class Meta:
        verbose_name_plural="图片"

