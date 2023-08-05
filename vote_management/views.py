# Django Imports
from django.shortcuts import get_list_or_404
from django.shortcuts import render
from django.views import View, generic
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count

# Local Imports
from user_profile.views import UserRequiredMixin, UserDashboard, UserProfile
from admin_profile.views import AdminRequiredMixin
from .models import VoteCard, VoteRecord, ElectedPerson, STATUS
from musa.forms import (UserVoteCardCreationForm,
                        AdminVoteCardCreationForm,
                        ElectedPersonForm)

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


# VOTE FUNCTIONALITY

class HomePageSingleView(View):
    """View for listing SINGLE VoteCards in homepage."""

    def get(self, request, slug, *args, **kwargs):
        queryset = VoteCard.objects.order_by('-created_on')
        card = get_object_or_404(queryset, slug=slug)
        candidates = card.vote_candidate.all()

        # Check if user voted or not
        if request.user.is_authenticated:
            has_voted = VoteRecord.objects.filter(
                voter=request.user, vote_card=card).exists()
        else:
            has_voted = False

        # Count the votes for each candidate
        vote_counts = VoteRecord.objects.filter(vote_card=card).values(
            'elected_person__name').annotate(vote_count=Count(
                'elected_person')).order_by('-vote_count')

        winner = vote_counts.first()
        challengers = vote_counts[1:]

        return render(request, "single_card.html",
                      {
                          "card": card,
                          "winner": winner,
                          "challengers": challengers,
                          "candidates": candidates,
                          "has_voted": has_voted,
                          "user_authenticated": request.user.is_authenticated
                      })

    def post(self, request, slug, *args, **kwargs):
        card = get_object_or_404(VoteCard, slug=slug, status=1)
        elected_person_id = request.POST.get('elected_person')

        # Check & Update Card if expired and set to 'Complete':
        card.update_card()

        if card.status == 3:

            # Selected winner based on higher votes
            vote_counts = VoteRecord.objects.filter(vote_card=card).values(
                'elected_person').annotate(vote_count=Count('elected_person')).order_by('-vote_count')

            winner_id = vote_counts.first()['elected_person']

            elected_person = ElectedPerson.objects.get(id=winner_id)
            elected_person.is_elected = True
            elected_person.save()

            # Message when event is set to 'Completed'
            messages.error(
                request, 'This event has expired, therefore COMPLETED!')
            return redirect('card_single', slug=card.slug)

        # Check if user has already voted
        if VoteRecord.objects.filter(
                voter=request.user, vote_card=card).exists():
            messages.error(request, "You have already voted for this card!")
            return redirect('card_single', slug=card.slug)

        # Make a vote based on these conditions or ask them to verify account
        elected_person = ElectedPerson.objects.get(id=elected_person_id)
        if request.user.verified == 1:
            VoteRecord.objects.create(
                voter=request.user,
                vote_card=card, elected_person=elected_person)
            messages.success(
                request, "Congratulations! Your vote has been recorded!")
        else:
            messages.error(
                request, "Verify your account!")

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
        queryset = VoteCard.objects.order_by('-created_on')
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


class AdminBaseListView(AdminRequiredMixin, generic.ListView):
    """Base view for listing VoteCards based on certain conditions."""
    model = VoteCard
    paginate_by = 10

    def get_queryset(self):
        """Return VoteCards with a status of 1, ordered by creation date."""
        return VoteCard.objects.order_by('-created_on')


class AdminEventList(AdminBaseListView):
    """ Read all created Vote Cards on Admin's Dashboard"""
    template_name = 'backend/admin-dashboard/all_events.html'
    context_object_name = 'admin_all_events'


class AdminApprovalList(AdminBaseListView):
    """ List to filter Vote Cards as draft for approval """
    template_name = 'backend/admin-dashboard/list_approve.html'
    context_object_name = 'admin_approval_list'

# ADMIN UPDATE card & READ card

# ADMIN READ Card


class AdminCardDetailView(AdminRequiredMixin, View):
    """View SINGLE created VoteCard from the admin Dashboard."""
    template_name = 'backend/admin-dashboard/single_card_admin.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = VoteCard.objects.order_by('-created_on')
        event = get_object_or_404(queryset, slug=slug)
        candidates = event.candidates.all()

        return render(request, "single_card_admin.html",
                      {
                          "event": event,
                          "candidates": candidates,
                          "user_authenticated": request.user.is_authenticated
                      })
# ADMIN UPDATE


class BaseAdminVoteCardDetailView(AdminRequiredMixin, View):
    """Base class for 'VoteCard detail view' with shared functionality."""

    template_name = None

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(slug)
        return render(request, self.template_name, context)

    def get_context_data(self, slug):
        queryset = VoteCard.objects.order_by('-created_on')
        event = get_object_or_404(queryset, slug=slug)
        status = STATUS
        candidates = event.candidates.all()
        return {
            "event": event,
            "candidates": candidates,
            "status": status,
            "user_authenticated": self.request.user.is_authenticated
        }


class AdminVoteCardDetailView(BaseAdminVoteCardDetailView):
    """Update SINGLE created VoteCard from the admin Dashboard."""
    template_name = 'backend/admin-dashboard/update.html'

    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(VoteCard, slug=slug)
        event.title = request.POST.get('title')
        status = request.POST.get('status')
        event.status = int(status)
        description = request.POST.get('description')
        event.description = description[:264]
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

# ADMIN Event Approval


class EventApprovalDetailView(AdminVoteCardDetailView):
    """Approve user's vote cards after on admin dashboard"""

    template_name = 'backend/admin-dashboard/approval.html'

    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(VoteCard, slug=slug)
        event.title = request.POST.get('title')
        status = request.POST.get('status')
        event.status = int(status)
        description = request.POST.get('description')
        event.description = description[:264]
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
