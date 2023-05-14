from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("signup", views.signUpPage, name="signup"),
    path("edit-profile", views.editProfilePage, name="edit-profile"),
    path("profile/<str:username>", views.ProfilePage, name="profile"),
]
