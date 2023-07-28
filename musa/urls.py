from django.urls import path
from . import views, role_redirect

urlpatterns = [
    # Backend
    path('login/', views.CustomLoginView.as_view(),
         name='account_login'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('user/', views.UserDashboard.as_view(),
         name='user_dashboard'),
    path('user/settings/', views.UserSettings.as_view(),
         name='user_settings'),
    path('user/password-change/', views.UserPasswordChangeView.as_view(),
         name='user_change'),
    path('user/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('office/', views.AdminDashboard.as_view(),
         name='admin_dashboard'),
    path('office/settings/', views.AdminSettings.as_view(),
         name='admin_settings'),
    path('office/password-change/', views.AdminPasswordChangeView.as_view(),
         name='admin_change'),
    path('role_redirect/', role_redirect.RoleRedirectView.as_view(),
         name='role_redirect'),

    # Frontend
    path('', views.HomePage.as_view(),
         name='homepage'),
    path('vote/<int:vote_card_id>/', views.VoteForCardView.as_view(),
         name='vote_for_card')
]
