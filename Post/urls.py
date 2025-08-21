from django.urls import path
from . import views

urlpatterns = [
    path('details/<slug:slug>', views.post_detail, name='Post_details'),
    path('list/', views.post_list, name="post-list"),
    path('search/', views.search, name="search"),

]
