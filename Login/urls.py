from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.Login, name='login'),
]