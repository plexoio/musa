# Django Imports
from django.views import View, generic
from django.utils import timezone

# Local Imports
from .models import UserProfile
from vote_management.models import VoteCard, VoteRecord, ElectedPerson
from vote_management.views import VoteCardBaseListView

# USER & ADMIN (General)

# USER Custom Message


class UserSuccess(generic.ListView):
    """Custom success message page for admin's or user's interaction"""
    model = UserProfile
    template_name = 'backend/user-dashboard/success.html'
    context_object_name = 'user_success'

# HOMEPAGE


class HomePage(VoteCardBaseListView):
    """Frontend main page displaying the list of VoteCards."""
    template_name = 'frontend/index.html'
    context_object_name = 'home_page'

    def progress_bar(self):
        """ It passes de VoteCard objects and progress bar data
        accessible with 'context_object_name' """
        vote_cards = self.get_queryset()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        vote_cards = self.get_queryset()
        context['official_vote_cards'] = [
            card for card in vote_cards if card.type == 1][:3]
        context['community_vote_cards'] = [
            card for card in vote_cards if card.type == 0][:3]
        context['now'] = timezone.now()

        return context

# TERMS & CONDITIONS PAGE


class TermsView(generic.ListView):
    ''' Implemented terms & conditions view ready for adjustments '''
    model = UserProfile
    template_name = "frontend/terms_conditions.html"
    context_object_name = 'terms_page'

# PRIVACY POLICY PAGE


class PrivacyView(generic.ListView):
    ''' Implemented privacy policy view ready for adjustments '''
    model = UserProfile
    template_name = "frontend/privacy_policy.html"
    context_object_name = 'privacy_page'

# CONTACT FORM


class ContactView(generic.ListView):
    ''' Implemented contact view ready for adjustments '''
    model = UserProfile
    template_name = "frontend/contact.html"
    context_object_name = 'contact_form'

# FAQ


class FAQView(generic.ListView):
    ''' Implemented FAQ view ready for adjustments '''
    model = UserProfile
    template_name = "frontend/faq.html"
    context_object_name = 'faq_page'
