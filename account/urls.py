from django.urls import path

from . import views

app_name = 'registration'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile_list/<int:pk>/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/<int:pk>/profile_edit', views.ProfileUpdateView.as_view(), name='profile_edit'),
    # path('signup/', views.signup, name='signup'),
    # path('activate/<uid>/', views.activate, name='activate'),
]
