from django.shortcuts import render
from django.views import generic
from .models import VoteCard, UserProfile

# Backend Controllers


class BaseListView(generic.ListView):
    model = VoteCard
    paginate_by = 6

    def get_queryset(self):
        return VoteCard.objects.filter(status=1).order_by('-created_on')


class UserDashboard(BaseListView):
    template_name = 'backend/user-dashboard/index.html'
    context_object_name = 'user_cards'


class UserSetting(generic.ListView):
    model = UserProfile
    template_name = 'backend/user-dashboard/settings.html'
    context_object_name = 'user_setting'


class AdminDashboard(BaseListView):
    template_name = 'backend/admin-dashboard/index.html'
    context_object_name = 'admin_cards'


class AdminSetting(generic.ListView):
    model = UserProfile
    template_name = 'backend/admin-dashboard/settings.html'
    context_object_name = 'admin_setting'


# Frontend Controllers

class HomePage(BaseListView):
    template_name = 'frontend/index.html'
    context_object_name = 'home_page'
