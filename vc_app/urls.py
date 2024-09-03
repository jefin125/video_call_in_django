from django.urls import path
from . import views

urlpatterns = [
    path('',views.SignUp,name="signup"),
    path('login/',views.user_login,name="login"),
    path('dashboard/',views.dashboard,name="dash"),
    path('logout/',views.user_logout,name="logout"),
    path('meeting/',views.meeting,name="meeting"),
    path('join/',views.join_room,name="join"),

]