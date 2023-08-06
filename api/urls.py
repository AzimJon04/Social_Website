from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserProfileList.as_view(), name='profile_list'),
    path('<int:pk>/', views.UserProfileDetail.as_view(), name="profile_detail"),
    path('posts/', views.PostPorfileList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostProfileDetail.as_view(), name='post_detail'),
]
