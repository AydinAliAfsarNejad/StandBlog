from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>', views.post_detail, name='Post_details'),
]