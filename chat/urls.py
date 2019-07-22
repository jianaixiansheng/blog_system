from django.urls import path
from chat import views

app_name='chat'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('info/<IP>/<int:PORT>/<name>/',views.info,name='info'),
    path('halo/',views.halo,name='halo')
]