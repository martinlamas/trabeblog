from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/comments/create', views.comment_create, name='comment_create')
]
