from django.urls import path
from . import views

urlpatterns = [
    path('test-users/create/', views.create_test_user, name='create_test_user'),
    path('test-users/', views.list_test_users, name='list_test_users'),
    path('admin-login/', views.admin_login, name='admin_login'),
]
