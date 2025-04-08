
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("profile", views.profile, name="profile"),
    path("follow/<int:user_id>", views.follow, name="follow"),
    path("userPosts/<int:user_id>", views.userPosts, name="userPosts"),
    path("following", views.followingView, name="followingView"),
    path("like/<int:post_id>", views.like, name="like"),
    path("edit/<int:post_id>", views.edit, name="edit")
]
