from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.UserProfileLogin.as_view(), name="user_login"),
    path(
        'login/user/', views.VoteCardUserDashboard.as_view(
        ), name="user_dashboard"),
    path('login/user/settings/', views.UserProfileSettings.as_view(), name="user_settings")
]
