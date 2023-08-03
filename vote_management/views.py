from django.shortcuts import render
from django.views import View, generic
from .models import VoteCard, VoteRecord, ElectedPerson
from musa.forms import (UserVoteCardCreationForm,
                        AdminVoteCardCreationForm,
                        ElectedPersonForm)
from django.forms import inlineformset_factory
from user_profile.views import UserRequiredMixin, UserDashboard
from admin_profile.views import AdminRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


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

# HOMEPAGE


class BaseListView(generic.ListView):
    """Base view for listing VoteCards based on certain conditions."""
    model = VoteCard
    paginate_by = 3

    def get_queryset(self):
        """Return VoteCards with a status of 1, ordered by creation date."""
        return VoteCard.objects.filter(status=1).order_by('-created_on')


class ListViewDetailed(BaseListView):
    """Base view for listing VoteCards."""
    template_name = 'frontend/all_cards.html'
    paginate_by = 6
    context_object_name = 'see_more'

    def get_queryset(self):
        """Return VoteCards with a status of 1, ordered by creation date."""
        return VoteCard.objects.filter(status=1).order_by('-created_on')


class ListViewDetailedOfficial(BaseListView):
    """Base view for listing Official VoteCards."""
    template_name = 'frontend/official_cards.html'
    paginate_by = 6
    context_object_name = 'see_more_official'

    def get_queryset(self):
        """VoteCards with a status of 1 and type 1, ordered by creation."""
        return VoteCard.objects.filter(
            type=1, status=1).order_by('-created_on')


class ListViewDetailedCommunity(BaseListView):
    """Base view for listing Official VoteCards."""
    template_name = 'frontend/community_cards.html'
    paginate_by = 6
    context_object_name = 'see_more_community'

    def get_queryset(self):
        """VoteCards with a status of 1 and type 0, ordered by creation."""
        return VoteCard.objects.filter(
            type=0, status=1).order_by('-created_on')


class SingleView(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = VoteCard.objects.filter(status=1)
        card = get_object_or_404(queryset, slug=slug)
        candidates = card.candidates.all()

        if request.user.is_authenticated:
            has_voted = VoteRecord.objects.filter(
                voter=request.user, vote_card=card).exists()
        else:
            has_voted = False

        return render(request, "single_card.html",
                      {
                          "card": card,
                          "candidates": candidates,
                          "has_voted": has_voted,
                          "user_authenticated": request.user.is_authenticated
                      })

    def post(self, request, slug, *args, **kwargs):

        card = get_object_or_404(VoteCard, slug=slug, status=1)

        elected_person_id = request.POST.get('elected_person')

        if VoteRecord.objects.filter(
                voter=request.user, vote_card=card).exists():
            messages.error(request, "You have already voted for this card!")
            return redirect('card_single', slug=card.slug)

        elected_person = ElectedPerson.objects.get(id=elected_person_id)

        VoteRecord.objects.create(
            voter=request.user, vote_card=card, elected_person=elected_person)

        messages.success(
            request, "Congratulations! Your vote has been recorded!")
        return redirect('card_single', slug=card.slug)


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
        form = UserVoteCardCreationForm(initial={'author': request.user})
        ElectedPersonFormSet = inlineformset_factory(
            VoteCard, ElectedPerson, form=ElectedPersonForm, extra=0)
        person_formset = ElectedPersonFormSet(
            queryset=ElectedPerson.objects.none())
        return render(
            request, self.template_name, {'form': form,
                                          'person_formset': person_formset})

    def post(self, request, *args, **kwargs):
        form = UserVoteCardCreationForm(request.POST, request.FILES)
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
        form = AdminVoteCardCreationForm(initial={'author': request.user})
        ElectedPersonFormSet = inlineformset_factory(
            VoteCard, ElectedPerson, form=ElectedPersonForm, extra=0)
        person_formset = ElectedPersonFormSet(
            queryset=ElectedPerson.objects.none())
        return render(
            request, self.template_name, {'form': form,
                                          'person_formset': person_formset})

    def post(self, request, *args, **kwargs):
        form = AdminVoteCardCreationForm(request.POST, request.FILES)
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
