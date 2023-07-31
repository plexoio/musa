from django.shortcuts import render
from django.views import View, generic
from .models import VoteCard, VoteRecord, ElectedPerson
from musa.forms import VoteCardCreationForm, ElectedPersonForm
from django.forms import inlineformset_factory
from user_profile.views import UserRequiredMixin, UserDashboard
from admin_profile.views import AdminRequiredMixin
from django.shortcuts import get_object_or_404, redirect


class VoteForCardView(View):
    """Voting mechanism to handle the voting action for a particular card."""

    def get(self, request, vote_card_id):
        vote_card = get_object_or_404(VoteCard, id=vote_card_id)
        user = request.user

        # Check if the user has already voted for this VoteCard
        if user in vote_card.vote_record.all():
            return redirect('already_voted')

        # Create a new VoteRecord instance if the user hasn't voted yet
        VoteRecord.objects.create(
            voter=user, vote_card=vote_card, elected_person=None)

        return redirect('vote_success')


class BaseListView(generic.ListView):
    """Base view for listing VoteCards based on certain conditions."""
    model = VoteCard
    paginate_by = 6

    def get_queryset(self):
        """Return VoteCards with a status of 1, ordered by creation date."""
        return VoteCard.objects.filter(status=1).order_by('-created_on')


# USER Event Management

# READ Event

class UserEventList(UserDashboard):
    """ Read all created Vote Cards on Admin's Dashboard"""
    template_name = 'backend/user-dashboard/all_events.html'
    context_object_name = 'user_all_events'

# CREATE Event


class UserVoteCardCreation(UserRequiredMixin, View):
    """ Create User's Vote Card instances for voting """
    template_name = 'backend/user-dashboard/create.html'

    def get(self, request, *args, **kwargs):
        form = VoteCardCreationForm(initial={'author': request.user})
        ElectedPersonFormSet = inlineformset_factory(
            VoteCard, ElectedPerson, form=ElectedPersonForm, extra=0)
        person_formset = ElectedPersonFormSet(
            queryset=ElectedPerson.objects.none())
        return render(
            request, self.template_name, {'form': form,
                                          'person_formset': person_formset})

    def post(self, request, *args, **kwargs):
        form = VoteCardCreationForm(request.POST, request.FILES)
        ElectedPersonFormSet = inlineformset_factory(
            VoteCard, ElectedPerson, form=ElectedPersonForm, extra=0)
        person_formset = ElectedPersonFormSet(
            request.POST, queryset=ElectedPerson.objects.none())

        if form.is_valid() and person_formset.is_valid():
            vote_card = form.save(commit=False)
            vote_card.author = request.user
            vote_card.save()

            person_formset.instance = vote_card
            person_formset.save()

            return redirect('user_success')
        else:
            return render(
                request, self.template_name,
                {'form': form, 'person_formset': person_formset})

# ADMIN Event Management

# READ Event


class AdminBaseListView(generic.ListView):
    """Base view for listing VoteCards based on certain conditions."""
    model = VoteCard
    paginate_by = 10

    def get_queryset(self):
        """Return VoteCards with a status of 1, ordered by creation date."""
        return VoteCard.objects.order_by('-created_on')


class AdminEventList(AdminRequiredMixin, AdminBaseListView):
    """ Read all created Vote Cards on Admin's Dashboard"""
    template_name = 'backend/admin-dashboard/all_events.html'
    context_object_name = 'admin_all_events'

# CREATE Event


class AdminVoteCardCreation(AdminRequiredMixin, View):
    """ Create Admin's Vote Card instances for voting """
    template_name = 'backend/admin-dashboard/create.html'

    def get(self, request, *args, **kwargs):
        form = VoteCardCreationForm(initial={'author': request.user})
        ElectedPersonFormSet = inlineformset_factory(
            VoteCard, ElectedPerson, form=ElectedPersonForm, extra=0)
        person_formset = ElectedPersonFormSet(
            queryset=ElectedPerson.objects.none())
        return render(
            request, self.template_name, {'form': form,
                                          'person_formset': person_formset})

    def post(self, request, *args, **kwargs):
        form = VoteCardCreationForm(request.POST, request.FILES)
        ElectedPersonFormSet = inlineformset_factory(
            VoteCard, ElectedPerson, form=ElectedPersonForm, extra=0)
        person_formset = ElectedPersonFormSet(
            request.POST, queryset=ElectedPerson.objects.none())

        if form.is_valid() and person_formset.is_valid():
            vote_card = form.save(commit=False)
            vote_card.author = request.user
            vote_card.save()

            person_formset.instance = vote_card
            person_formset.save()

            return redirect('user_success')
        else:
            return render(
                request, self.template_name,
                {'form': form, 'person_formset': person_formset})
