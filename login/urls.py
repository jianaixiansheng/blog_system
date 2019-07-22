
from login import views
from django.urls import path

app_name='logins'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.login, name='login'),
    path('code/', views.verify_code, name='code'),
    path('forget/',views.forgetpassword,name='forget'),
    path('change/',views.change,name='change'),
    path('zhuce/',views.zhuce,name='zhuce'),
]

