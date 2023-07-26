from . import views
from django.urls import path

urlpatterns = [
    # Backend
    path('user/', views.UserDashboard.as_view(
    ), name="user_dashboard"),
    path('user/settings/', views.UserSetting.as_view(
    ), name="user_settings"),
    path('office/', views.AdminDashboard.as_view(
    ), name="admin_dashboard"),
    path('office/settings/', views.AdminSetting.as_view(
    ), name="admin_settings"),

    # Frontend
    path('', views.HomePage.as_view(
    ), name="homepage")
]
