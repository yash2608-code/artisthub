from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # Pages
    path("", views.IndexPage, name="indexpage"),
    path("register-page/", views.RegisterPage, name="register-page"),
    path("login-page/", views.LoginPage, name="login-page"),
    path("dashboard-page/", views.DashBoardPage, name="dashboard-page"),
    path("dashboard-setting/<int:pk>/", views.DashBoardSettingPage,
         name="dashboard-setting"),
    path("all-artist/",views.AllArtistPage,name="allartist"),
    path("artist-profile/<int:pk>/",views.ArtistProfile,name="artpro"),
    path("book-artist/<int:pk>/",views.BookArtistPage,name="book-artist"),
    path("my-work-request/",views.MyWorkReq,name="myworkreq"),
    path("register/", views.RegisterUser, name="register"),
    path("login/", views.LoginUser, name="login"),
    path("logout/", views.LogOut, name="logout"),
    path("update/<int:pk>/", views.UpdateUser, name="update-user"),
    path("artist-booking/<int:pk>/",views.BookArtist,name="bookartist"),
]
