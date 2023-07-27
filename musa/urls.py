from django.urls import path
from . import views

urlpatterns = [
    # Backend
    path('accounts/login/', views.CustomLoginView.as_view(), name='account_login'),
    path('user/', views.UserDashboard.as_view(), name="user_dashboard"),
    path('user/settings/', views.UserSettings.as_view(), name="user_settings"),
    path('office/', views.AdminDashboard.as_view(), name="admin_dashboard"),
    path('office/settings/', views.AdminSettings.as_view(), name="admin_settings"),

    # Frontend
    path('', views.HomePage.as_view(), name="homepage"),
    path('vote/<int:vote_card_id>/',
         views.VoteForCardView.as_view(), name='vote_for_card')
]
