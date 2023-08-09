# Django imports
from django.urls import path

# Local relative imports
from . import views, role_redirect

# Authentication app imports
from authentication.views import (CustomLoginView, CustomSignupView,
                                  CustomLogoutView)

# User Profile app imports
from user_profile.views import (UserDashboard,
                                UserSettings,
                                UserPasswordChangeView,
                                UserDelete,
                                UserRole)

# Admin Profile app imports
from admin_profile.views import (AdminDashboard, AdminSettings,
                                 AdminPasswordChangeView,
                                 AdminRole)

# Vote Management app imports
from vote_management.views import (UserVoteCardCreation, AdminVoteCardCreation,
                                   AdminEventList, UserEventList,
                                   AllVoteCardsListView, HomePageSingleView,
                                   OfficialVoteCardsListView,
                                   CommunityVoteCardsListView,
                                   AdminVotes, UserVotes, UserSingleView,
                                   AdminVoteCardDetailView,
                                   AdminSingleView,
                                   EventApprovalDetailView,
                                   AdminApprovalList,
                                   CompletedVoteCardsListView)

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
    path('user/votes/', UserVotes.as_view(),
         name='user_votes'),
    path('user/single/<slug:slug>/', UserSingleView.as_view(),
         name='user_single'),

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
    path('office/votes', AdminVotes.as_view(),
         name='admin_votes'),
    path('office/single/card/<slug:slug>/', AdminSingleView.as_view(),
         name='admin_single'),
    path('office/update/<slug:slug>/', AdminVoteCardDetailView.as_view(),
         name='admin_card_update'),
    path('office/all/approve/', AdminApprovalList.as_view(),
         name='admin_approval_list'),
    path('office/approval/<slug:slug>/', EventApprovalDetailView.as_view(),
         name='admin_approval'),

    # ROLE
    path('role_redirect/', role_redirect.RoleRedirectView.as_view(),
         name='role_redirect'),

    # FRONTEND
    path('', views.HomePage.as_view(),
         name='homepage'),
    path('<slug:slug>', HomePageSingleView.as_view(),
         name='card_single'),
    path('all/', AllVoteCardsListView.as_view(),
         name='see_more'),
    path('all/official/', OfficialVoteCardsListView.as_view(),
         name='see_more_official'),
    path('all/community/', CommunityVoteCardsListView.as_view(),
         name='see_more_community'),
    path('all/completed/', CompletedVoteCardsListView.as_view(),
         name='see_more_completed'),
    path('contact/', views.ContactView.as_view(),
         name='contact_form'),
    path('faq/', views.FAQView.as_view(),
         name='faq_page'),
    path('terms/', views.TermsView.as_view(),
         name='terms_page'),
    path('policy/', views.PrivacyView.as_view(),
         name='policy_page')
]
