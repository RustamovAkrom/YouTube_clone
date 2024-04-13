from django.contrib import admin
from django.urls import path, include
from apps.users.views import RegisterView, LoginView, LogoutView


app_name = "users"
urlpatterns = [
    path('Registration/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
