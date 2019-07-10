
from login import views
from django.urls import path

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views._login,name='login'),
    path('code/', views.verify_code, name='code'),
    path('forget/',views.forgetpassword,name='forget'),
    path('change/',views.change,name='change')
]

