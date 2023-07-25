from django.shortcuts import render
from django.views import generic
from .models import VoteCard, UserProfile


class UserDashboard(generic.ListView):
    model = VoteCard
    queryset = VoteCard.objects.filter(status=1).order_by('-created_on')
    template_name = 'backend/user-dashboard/index.html'
    paginate_by = 6


class UserSetting(generic.ListView):
    model = UserProfile
    template_name = 'backend/user-dashboard/settings.html'


class AdminDashboard(generic.ListView):
    model = VoteCard
    queryset = VoteCard.objects.filter(status=1).order_by('-created_on')
    template_name = 'backend/admin-dashboard/index.html'
    paginate_by = 6


class AdminSetting(generic.ListView):
    model = UserProfile
    template_name = 'backend/admin-dashboard/settings.html'
