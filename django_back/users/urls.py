from django.urls import path
from rest_framework.authtoken import views as rest_views
from . import views


urlpatterns = [
    path('all/', views.users_list, name="users"),
    path('register/', views.UserCreate.as_view(), name="register"),
    path('login/', rest_views.obtain_auth_token, name="login"),
]