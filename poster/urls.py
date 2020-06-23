from django.urls import path
from poster import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('boasts/', views.boasts, name='boasts'),
    path('roasts/', views.roasts, name='roasts'),
    path('detail_like/<int:pk>/', views.detail_like_view,
         name='detail_like_post'),
    path('detail_dislike/<int:pk>/', views.detail_dislike_view,
         name='detail_dislike_post'),
    path('posts/like/<int:pk>/', views.posts_like_view,
         name='posts_like_post'),
    path('posts/dislike/<int:pk>/', views.posts_dislike_view,
         name='posts_dislike_post'),
    path('boasts/like/<int:pk>/', views.boasts_like_view,
         name='boasts_like_post'),
    path('boasts/dislike/<int:pk>/', views.boasts_dislike_view,
         name='boasts_dislike_post'),
    path('roasts/like/<int:pk>/', views.roasts_like_view,
         name='roasts_like_post'),
    path('roasts/dislike/<int:pk>/', views.roasts_dislike_view,
         name='roasts_dislike_post'),
    path('new_post/', views.new_post_view, name="new_post")




]
