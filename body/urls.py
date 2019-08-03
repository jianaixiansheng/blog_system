from django.urls import path,include
from body import views

app_name='body'

urlpatterns = [
    path('index/', views.index, name='index'), # 首页
    path('dynamic_state/', views.dynamic_state, name='dynamic_state'), # 动态
    path('music/', views.music, name='music'), # 音乐
    # path('photo_album/', views.photo_album, name='photo_album'), # 相册
    path('personal/', views.personal, name='personal'), # 个人档
    path('chat/', views.chat, name='chat'), # 聊天系统
    path('publish/', views.publish1.as_view(), name='publish'),
    path('Love_article/', views.Love_article2, name='Love_article2'),
    path('move_text1/', views.move_text1, name='move_text1'),
    path('comment/', views.Commnets, name='Comment'),
    path('thumps_up2', views.thumps_up2, name='thumps_up2'),
    path('indexs/<int:us_id>/',views.indexs,name='indexs'),
    path('qiandao/',views.qiandao,name='qiandao'),
    path('guanzhu/',views.guanzhu,name='guanzhu'),
    path('noguanzhu/',views.noguanzhu,name='noguanzhu'),
    path('Comments_2/', views.Comments_2, name='Comments_2'),
    path('publish/', views.publish1.as_view(), name='publish'),
    path('move_text1/', views.move_text1, name='move_text1'),
    path('Love_article2/', views.Love_article2, name='Love_article2'),
    # path('get_page/', views.get_page, name='get_page'),
]

