from django.urls import path
from . import views
from django.contrib import admin

from django.views.generic import RedirectView
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import update_profile

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
  
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('home/', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    #path('<str:room>/', views.room, name='room'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('notification', views.notification, name='notification'),
    path('matches', views.matches, name='matches'),
    path('logout/', views.logout, name='logout'),
    path('navbar_card/', views.navbar_card, name='navbar_card'),
    path('upgrade_card/', views.upgrade_card, name='upgrade_card'),
    path("logoutpage/", views.LogoutPage, name="logoutpage"),
    path("user/", views.HomePage, name="homepage"),
    path("edit/", views.EditProfile, name="edit"),
    path("user/<str:username>/", views.userprofile, name="username"),
    path("add_friend/", views.add_friend, name="add_friend"),
    path("accept_request/", views.accept_request, name="accept_request"),
    path("delete_friend/", views.delete_friend, name="delete_friend"),
    path("search/", views.search, name="search"),
    path('chat/<str:username>/', views.chat, name='chat'),
    path("looking_for/", views.looking_for, name="looking_for"),
    path('searchpage', views.searchpage, name='searchpage'),
    path('upgrade', views.upgrade, name='upgrade'),
    path('messagess', views.messagess, name='messagess'),
    path("loginpage/", views.LoginPage, name="loginpage"),
    #path("signuppage/", views.SignupPage, name="signuppage"),
    path('user/<str:username>/', views.userprofile, name='username'),
    re_path(r"^.*/$", RedirectView.as_view(pattern_name="login", permanent=False)),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    
    path('userprofile/<str:username>/', views.userprofile, name='userprofile'),
    

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)