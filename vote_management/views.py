from django.shortcuts import get_list_or_404
from django.shortcuts import render
from django.views import View, generic
from .models import VoteCard, VoteRecord, ElectedPerson
from musa.forms import (UserVoteCardCreationForm,
                        AdminVoteCardCreationForm,
                        ElectedPersonForm)
from django.forms import inlineformset_factory
from user_profile.views import UserRequiredMixin, UserDashboard, UserProfile
from admin_profile.views import AdminRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# HOMEPAGE DISPLAY


class VoteCardBaseListView(generic.ListView):
    """Base view for listing VoteCards based on these conditions."""
    model = VoteCard
    paginate_by = 3

    def get_queryset(self):
        """Return VoteCards with a status of 1, ordered by creation date."""
        return VoteCard.objects.filter(status=1).order_by('-created_on')


class AllVoteCardsListView(VoteCardBaseListView):
    """Base view for listing ALL VoteCards."""
    template_name = 'frontend/all_cards.html'
    paginate_by = 6
    context_object_name = 'see_more'

    def get_queryset(self):
        """Return VoteCards with a status of 1, ordered by creation date."""
        return VoteCard.objects.filter(status=1).order_by('-created_on')


class OfficialVoteCardsListView(VoteCardBaseListView):
    """Base view for listing ONLY Official VoteCards."""
    template_name = 'frontend/official_cards.html'
    paginate_by = 6
    context_object_name = 'see_more_official'

    def get_queryset(self):
        return VoteCard.objects.filter(
            type=1, status=1).order_by('-created_on')


class CommunityVoteCardsListView(VoteCardBaseListView):
    """Base view for listing ONLY Community VoteCards."""
    template_name = 'frontend/community_cards.html'
    paginate_by = 6
    context_object_name = 'see_more_community'

    def get_queryset(self):
        return VoteCard.objects.filter(
            type=0, status=1).order_by('-created_on')


class HomePageSingleView(View):
    """View for listing SINGLE VoteCards in homepage."""

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


# USER Dashboard - Event Management

# USER READ Event


class UserEventList(UserDashboard):
    """ Read all created Vote Cards on Admin's Dashboard"""
    template_name = 'backend/user-dashboard/all_events.html'
    context_object_name = 'user_all_events'

# USER Single Card Display


class UserSingleView(UserRequiredMixin, View):
    """View for listing SINGLE VoteCard on the user Dashboard."""

    def get(self, request, slug, *args, **kwargs):
        queryset = VoteCard.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        candidates = event.candidates.all()

        if request.user.is_authenticated:
            has_voted = VoteRecord.objects.filter(
                voter=request.user, vote_card=event).exists()
        else:
            has_voted = False

        return render(request, "single_card_user.html",
                      {
                          "event": event,
                          "candidates": candidates,
                          "has_voted": has_voted,
                          "user_authenticated": request.user.is_authenticated
                      })


# USER CREATE Event


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

# USER Votes Display


class UserVotes(UserRequiredMixin, generic.ListView):
    model = VoteRecord
    template_name = 'backend/user-dashboard/user_votes.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_votes = VoteRecord.objects.filter(
            voter=self.request.user).order_by('-timestamp')
        context['user_votes'] = user_votes
        return context


# ADMIN Dashboard - Event Management

# ADMIN READ Event


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

# ADMIN UPDATE card & READ card

# ADMIN READ Card


class AdminCardDetailView(AdminRequiredMixin, View):
    """View SINGLE created VoteCard from the admin Dashboard."""
    template_name = 'backend/admin-dashboard/single_card_admin.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = VoteCard.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        candidates = event.candidates.all()

        return render(request, "single_card_admin.html",
                      {
                          "event": event,
                          "candidates": candidates,
                          "user_authenticated": request.user.is_authenticated
                      })
# ADMIN UPDATE


class AdminVoteCardDetailView(AdminRequiredMixin, View):
    """Update SINGLE created VoteCard from the admin Dashboard."""
    template_name = 'backend/admin-dashboard/update.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = VoteCard.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        candidates = event.candidates.all()

        return render(request, "update.html",
                      {
                          "event": event,
                          "candidates": candidates,
                          "user_authenticated": request.user.is_authenticated
                      })

    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(VoteCard, slug=slug, status=1)
        description = request.POST.get('description')
        event.description = description[:264]
        event.title = request.POST.get('title')
        event.mission = request.POST.get('mission')
        event.location = request.POST.get('location')

        uploaded_image = request.FILES.get(
            'event_image')
        if uploaded_image:
            upload = upload(uploaded_image)
            event.event_image = upload['url']

        event.save()
        messages.success(
            request, "Congratulations! The VoteCard has been Updated!")
        return redirect('admin_card_update', slug=event.slug)

# ADMIN CREATE Event


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

# ADMIN VOTES


class AdminVotes(AdminRequiredMixin, generic.ListView):
    """Return VoteCard Votes with a status of 1, ordered by creation date."""
    model = VoteRecord
    template_name = 'backend/admin-dashboard/admin_votes.html'
    paginate_by = 10
    context_object_name = 'admin_votes'

    def get_queryset(self):
        return VoteRecord.objects.order_by('-timestamp')
