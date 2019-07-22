from django.contrib import admin
from .models import UserInfo,DynamicStatus,Comment

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    '''用户信息管理类'''
    list_per_page = 100
    list_display = ['id','user_numbers','user_name',
                    'user_sex','user_sign','user_birth',
                    'user_city','user_one_level','user_member_level']
    actions_on_bottom = True
    actions_on_top = False


admin.site.register(UserInfo,UserInfoAdmin)


# class PhotoAlbumAdmin(admin.ModelAdmin):
#     '''图片信息管理类'''
#     list_per_page = 100
#     list_display = ['id','user_image','image_time','image_type']
#     actions_on_bottom = True
#     actions_on_top = False


# admin.site.register(PhotoAlbum, PhotoAlbumAdmin)

class DynamicStatusAdmin(admin.ModelAdmin):
    '''文章信息管理类'''
    list_per_page = 100
    list_display = ['id','user_id','new_content','d_like','d_num','d_picture','d_content','d_time']
    actions_on_bottom = True
    actions_on_top = False


admin.site.register(DynamicStatus, DynamicStatusAdmin)

class CommentAdmin(admin.ModelAdmin):
    '''评论信息管理类'''
    list_per_page = 100
    list_display = ['id']
    actions_on_bottom = True
    actions_on_top = False


admin.site.register(Comment, CommentAdmin)