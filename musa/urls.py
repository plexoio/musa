from django.urls import path
from . import views, role_redirect

urlpatterns = [
    # BACKEND
    path('login/', views.CustomLoginView.as_view(),
         name='account_login'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    # USER
    path('user/', views.UserDashboard.as_view(),
         name='user_dashboard'),
    path('user/settings/', views.UserSettings.as_view(),
         name='user_settings'),
    path('user/password-change/', views.UserPasswordChangeView.as_view(),
         name='user_change'),
    path('user/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('user/create', views.VoteCardCreation.as_view(),
         name='event_creation'),
    path('user/success', views.UserSuccess.as_view(),
         name='user_success'),

    # OFFICE
    path('office/', views.AdminDashboard.as_view(),
         name='admin_dashboard'),
    path('office/settings/', views.AdminSettings.as_view(),
         name='admin_settings'),
    path('office/password-change/', views.AdminPasswordChangeView.as_view(),
         name='admin_change'),
    # ROLE
    path('role_redirect/', role_redirect.RoleRedirectView.as_view(),
         name='role_redirect'),

    # FRONTEND
    path('', views.HomePage.as_view(),
         name='homepage'),
    path('vote/<int:vote_card_id>/', views.VoteForCardView.as_view(),
         name='vote_for_card')
]
