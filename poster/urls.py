from django.urls import path
from poster import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('up_vote/<int:pk>/', views.up_vote_view),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    # path('post/<str:magic>/', views.post_detail,
    #      name="magic_detail"),
    path('boasts/', views.boasts, name='boasts'),
    path('roasts/', views.roasts, name='roasts'),
    path('detail_like/<int:pk>/', views.detail_like_view,
         name='detail_like_post'),
    path('detail_dislike/<int:pk>/', views.detail_dislike_view,
         name='detail_dislike_post'),


]
