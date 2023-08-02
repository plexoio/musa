# THE NEW ORDER
from .models import UserProfile
from vote_management.models import VoteCard, VoteRecord, ElectedPerson
from vote_management.views import BaseListView
from django.views import View, generic

# USER

# USER Success


class UserSuccess(generic.ListView):
    model = UserProfile
    template_name = 'backend/user-dashboard/success.html'
    context_object_name = 'user_success'

# HOMEPAGE


class HomePage(BaseListView):
    """Frontend main page displaying the list of VoteCards."""
    template_name = 'frontend/index.html'
    context_object_name = 'home_page'

    def get_queryset(self):
        """Return all VoteCards."""
        return VoteCard.objects.all()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['official_vote_cards'] = VoteCard.objects.filter(type=1)[:3]
        context['community_vote_cards'] = VoteCard.objects.filter(type=0)[:3]

        return context
