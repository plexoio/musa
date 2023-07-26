from django.shortcuts import render
from allauth.account.views import LoginView
from django.views import View
from django.views import generic
from django.urls import reverse_lazy
from .models import VoteCard, UserProfile, VoteRecord
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Vote


class VoteForCardView(View):
    def get(self, request, vote_card_id):
        vote_card = get_object_or_404(VoteCard, id=vote_card_id)
        user = request.user

        # Check if the user has already voted for this VoteCard (optional)
        if user in vote_card.vote_record.all():
            # Handle the case when the user has already voted
            # You can redirect them to a different page or show an error message
            return redirect('already_voted')

        # If the user has not voted, create a new VoteRecord instance
        vote_record = VoteRecord.objects.create(
            voter=user, vote_card=vote_card, elected_person=None)

        # Optionally, you can do additional processing here, such as updating the number_of_votes in VoteCard

        return redirect('vote_success')


# Backend Controllers


class BaseListView(generic.ListView):
    model = VoteCard
    paginate_by = 6

    def get_queryset(self):
        return VoteCard.objects.filter(status=1).order_by('-created_on')


class CustomLoginView(LoginView):
    def get_success_url(self):
        user_id = self.request.user.id
        return reverse('user_dashboard', kwargs={'pk': user_id})


class UserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user_profile = self.request.user

        if user_profile.is_authenticated and user_profile.role == 0:
            return True
        return False


class UserDashboardCards(UserRequiredMixin, LoginRequiredMixin, BaseListView):
    template_name = 'backend/user-dashboard/index.html'
    context_object_name = 'user_cards'

    def get_queryset(self):
        user_id = self.request.user.id
        return VoteCard.objects.filter(author_id=user_id, status=1).order_by('-created_on')


class UserDashBoard(UserRequiredMixin, LoginRequiredMixin, generic.DetailView):
    model = UserProfile
    template_name = 'backend/user-dashboard/index.html'
    context_object_name = 'user_data'


class AdminRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        user_profile = self.request.user
        if user_profile and user_profile.role == 2:
            return True
        return False


class AdminDashboard(AdminRequiredMixin, BaseListView):
    template_name = 'backend/admin-dashboard/index.html'
    context_object_name = 'admin_cards'


class AdminSetting(AdminRequiredMixin, generic.ListView):
    model = UserProfile
    template_name = 'backend/admin-dashboard/settings.html'
    context_object_name = 'admin_setting'


# Frontend Controllers

class HomePage(BaseListView):
    template_name = 'frontend/index.html'
    context_object_name = 'home_page'
