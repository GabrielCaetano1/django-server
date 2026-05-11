from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_users, name='list_users'),
    path('new/', views.create_user, name='create_user'),
    path('<int:pk>/edit/', views.edit_user, name='edit_user'),
    path('<int:pk>/delete/', views.delete_user, name='delete_user'),
]