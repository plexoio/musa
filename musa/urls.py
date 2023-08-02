# Django imports
from django.urls import path

# Local relative imports
from . import views, role_redirect

# Authentication app imports
from authentication.views import CustomLoginView, CustomSignupView, CustomLogoutView

# User Profile app imports
from user_profile.views import UserDashboard, UserSettings, UserPasswordChangeView, UserDelete, UserRole

# Admin Profile app imports
from admin_profile.views import AdminDashboard, AdminSettings, AdminPasswordChangeView, AdminRole

# Vote Management app imports
from vote_management.views import (UserVoteCardCreation,
                                   AdminVoteCardCreation,
                                   VoteForCardView,
                                   AdminEventList,
                                   UserEventList,
                                   ListViewDetailed,
                                   SingleView,
                                   ListViewDetailedOfficial,
                                   ListViewDetailedCommunity)

urlpatterns = [
    # AUTHENTICATION
    path('login/', CustomLoginView.as_view(),
         name='account_login'),
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # USER
    path('user/', UserDashboard.as_view(),
         name='user_dashboard'),
    path('user/settings/', UserSettings.as_view(),
         name='user_settings'),
    path('user/password-change/', UserPasswordChangeView.as_view(),
         name='user_change'),
    path('user/delete/', UserDelete.as_view(), name='user_delete'),
    path('user/all', UserEventList.as_view(),
         name='user_all_events'),
    path('user/role', UserRole.as_view(),
         name='user_role'),

    # VOTE MANAGEMENT
    path('user/create', UserVoteCardCreation.as_view(),
         name='user_creation'),

    # USER SUCCESS
    path('success/', views.UserSuccess.as_view(),
         name='user_success'),

    # OFFICE
    path('office/', AdminDashboard.as_view(),
         name='admin_dashboard'),
    path('office/settings/', AdminSettings.as_view(),
         name='admin_settings'),
    path('office/password-change/', AdminPasswordChangeView.as_view(),
         name='admin_change'),
    path('office/create', AdminVoteCardCreation.as_view(),
         name='admin_creation'),
    path('office/all', AdminEventList.as_view(),
         name='admin_all_events'),
    path('office/role', AdminRole.as_view(),
         name='admin_role'),

    # ROLE
    path('role_redirect/', role_redirect.RoleRedirectView.as_view(),
         name='role_redirect'),

    # FRONTEND
    path('', views.HomePage.as_view(),
         name='homepage'),
    path('all/', ListViewDetailed.as_view(),
         name='see_more'),
    path('all/official/', ListViewDetailedOfficial.as_view(),
         name='see_more_official'),
    path('all/community/', ListViewDetailedCommunity.as_view(),
         name='see_more_community'),
    path('<slug:slug>', SingleView.as_view(),
         name='card_single'),
    path('vote/<int:vote_card_id>/', VoteForCardView.as_view(),
         name='vote_for_card')
]
