from django.urls import path,include
from body import views

urlpatterns = [
    path('index/', views.index, name='index'), # 首页
    path('dynamic_state/', views.dynamic_state, name='dynamic_state'), # 动态
    path('music/', views.music, name='music'), # 音乐
    path('photo_album/', views.photo_album, name='photo_album'), # 相册
    path('personal/', views.personal, name='personal'), # 个人档
    path('chat/', views.chat, name='chat'), # 聊天系统
    path('', views.log, name='log'), # 登陆
    path('register/', views.register, name='register'), # 注册
    path('retrieve_password/', views.retrieve_password, name='retrieve_password'), # 找回密码
    path('change_password/', views.change_password, name='change_password'), # 修改密码
    path('publish/', views.publish.as_view(), name='publish'),
    path('thump_up/', views.Thumpsup, name='thumps_up')
]

