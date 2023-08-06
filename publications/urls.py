from django.urls import path

from . import views

app_name = 'publications'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<int:pk>/', views.post_user, name='post_user'),
]
