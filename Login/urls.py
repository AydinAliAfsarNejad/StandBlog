from django.urls import path
from . import views


app_name = 'login'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.Login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]