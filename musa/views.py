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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add the total vote count to the context
        context['total_votes'] = VoteRecord.objects.all().count()
        return context
