from django.shortcuts import render
from django.views import generic
from .models import VoteCard, UserProfile


class VoteCardUserDashboard(generic.ListView):
    model = VoteCard
    queryset = VoteCard.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class UserProfileLogin(generic.ListView):
    model = UserProfile
    template_name = 'login.html'


class UserProfileSettings(generic.ListView):
    model = UserProfile
    template_name = 'settings.html'
