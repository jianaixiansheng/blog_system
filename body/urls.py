from django.urls import path,include
from body import views

app_name='body'

urlpatterns = [
    path('index/', views.index, name='index'), # 首页
    path('dynamic_state/', views.dynamic_state, name='dynamic_state'), # 动态
    path('music/', views.music, name='music'), # 音乐
    path('photo_album/', views.photo_album, name='photo_album'), # 相册
    path('personal/', views.personal, name='personal'), # 个人档
    path('chat/', views.chat, name='chat'), # 聊天系统
    path('publish/', views.publish.as_view(), name='publish'),
    path('publish/', views.publish.as_view(), name='publish'),
    path('thump_up/<int:a_id>', views.Thumpsup, name='thumps_up'),
    path('Love_article/<int:a_id>', views.Love_article, name='Love_article'),
    path('move_text/<int:a_id>', views.move_text, name='move_text'),
    path('comment/', views.Commnets, name='Comment'),
    path('thumps_up2', views.thumps_up2, name='thumps_up2'),
    path('indexs/<int:us_id>',views.indexs,name='indexs'),
    path('attention/<int:us_id>',views.attention,name='attention'),
    # path('get_aid/<int:aid>', views.get_aid, name='get_aid')
]

