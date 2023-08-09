# Django Imports
from django.shortcuts import get_list_or_404
from django.shortcuts import render
from django.views import View, generic
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from django.utils import timezone


# Local Imports
from user_profile.views import UserRequiredMixin, UserDashboard, UserProfile
from admin_profile.views import AdminRequiredMixin
from .models import VoteCard, VoteRecord, ElectedPerson, STATUS
from musa.forms import (UserVoteCardCreationForm,
                        AdminVoteCardCreationForm,
                        ElectedPersonForm)
from .image_validation import validate_image_size

# HOMEPAGE DISPLAY


class VoteCardBaseListView(generic.ListView):
    """Base view for listing VoteCards based on these conditions."""
    model = VoteCard
    paginate_by = 3

    def get_queryset(self):
        """Return VoteCards with a status of 1, ordered by creation date."""
        vote_cards = VoteCard.objects.filter(status=1).order_by('-created_on')

        for vote_card in vote_cards:
            now = timezone.now().date()
            total_duration = 0.01 + \
                (vote_card.expire - vote_card.created_on).days
            elapsed_time = (now - vote_card.created_on).days
            vote_card.progress = format(
                (elapsed_time / total_duration) * 100, '.0f')
            vote_card.time_left = format(total_duration - elapsed_time, '.0f')
        return vote_cards


class AllVoteCardsListView(VoteCardBaseListView):
    """Base view for listing ALL VoteCards."""
    template_name = 'frontend/all_cards.html'
    paginate_by = 6
    context_object_name = 'see_more'

    def progress_bar(self):
        """ It passes de VoteCard objects and progress bar data
        accessible with 'context_object_name' """
        vote_cards = self.get_queryset()


class OfficialVoteCardsListView(VoteCardBaseListView):
    """Base view for listing ONLY Official VoteCards."""
    template_name = 'frontend/official_cards.html'
    paginate_by = 6
    context_object_name = 'see_more_official'

    def get_queryset(self):

        offical_cards = VoteCard.objects.filter(
            type=1, status=1).order_by('-created_on')

        for vote_card in offical_cards:
            now = timezone.now().date()
            total_duration = 0.01 + \
                (vote_card.expire - vote_card.created_on).days
            elapsed_time = (now - vote_card.created_on).days
            vote_card.progress = format(
                (elapsed_time / total_duration) * 100, '.0f')
            vote_card.time_left = format(
                total_duration - elapsed_time, '.0f')
        return offical_cards


class CommunityVoteCardsListView(VoteCardBaseListView):
    """Base view for listing ONLY Community VoteCards."""
    template_name = 'frontend/community_cards.html'
    paginate_by = 6
    context_object_name = 'see_more_community'

    def get_queryset(self):

        completed_cards = VoteCard.objects.filter(
            type=0, status=1).order_by('-created_on')

        for vote_card in completed_cards:
            now = timezone.now().date()
            total_duration = 0.01 + \
                (vote_card.expire - vote_card.created_on).days
            elapsed_time = (now - vote_card.created_on).days
            vote_card.progress = format(
                (elapsed_time / total_duration) * 100, '.0f')
            vote_card.time_left = format(
                total_duration - elapsed_time, '.0f')
        return completed_cards


class CompletedVoteCardsListView(VoteCardBaseListView):
    """Base view for listing ONLY Community VoteCards."""
    template_name = 'frontend/completed_cards.html'
    paginate_by = 6
    context_object_name = 'see_more_completed'

    def get_queryset(self):

        completed_cards = VoteCard.objects.filter(
            status=3).order_by('-created_on')

        for vote_card in completed_cards:
            now = timezone.now().date()
            total_duration = 0.01 + \
                (vote_card.expire - vote_card.created_on).days
            elapsed_time = (now - vote_card.created_on).days
            vote_card.progress = format(
                (elapsed_time / total_duration) * 100, '.0f')
            vote_card.time_left = format(
                total_duration - elapsed_time, '.0f')
        return completed_cards

# VOTE FUNCTIONALITY


class HomePageSingleView(View):
    """View for listing SINGLE VoteCards in homepage."""

    def get(self, request, slug, *args, **kwargs):
        queryset = VoteCard.objects.order_by('-created_on')
        card = get_object_or_404(queryset, slug=slug)
        candidates = card.vote_candidate.all()

        # Progress bar

        now = timezone.now().date()
        total_duration = 0.01 + \
            (card.expire - card.created_on).days
        elapsed_time = (now - card.created_on).days
        card.progress = format(
            (elapsed_time / total_duration) * 100, '.0f')
        card.time_left = format(
            total_duration - elapsed_time, '.0f')

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

        if request.user.verified == 1 and card.status == 3:

            # Selected winner based on higher votes
            vote_counts = VoteRecord.objects.filter(vote_card=card).values(
                'elected_person').annotate(vote_count=Count(
                    'elected_person')).order_by('-vote_count')

            winner_id = vote_counts.first()['elected_person']

            elected_person = ElectedPerson.objects.get(id=winner_id)
            elected_person.is_elected = True
            elected_person.save()

            # Message when event is set to 'Completed'
            messages.error(
                request, 'Event has expired & your vote was not recorded.')
            return redirect('card_single', slug=card.slug)

        # Check if user has already voted
        if VoteRecord.objects.filter(
                voter=request.user, vote_card=card).exists():
            messages.error(request, "You have already voted for this card!")
            return redirect('card_single', slug=card.slug)

        # Make a vote based on these conditions or ask them to verify account
        elected_person = ElectedPerson.objects.get(id=elected_person_id)
        if request.user.verified == 1 and card.status == 1:
            VoteRecord.objects.create(
                voter=request.user,
                vote_card=card, elected_person=elected_person)
            messages.success(
                request, "Congratulations! Your vote has been recorded!")
        else:
            messages.error(
                request, "Is your account verified and VoteCard online?")

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

        # Progress bar

        now = timezone.now().date()
        total_duration = 0.01 + \
            (event.expire - event.created_on).days
        elapsed_time = (now - event.created_on).days
        event.progress = format(
            (elapsed_time / total_duration) * 100, '.0f')
        event.time_left = format(
            total_duration - elapsed_time, '.0f')

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

        # Check the image size here
        uploaded_image = request.FILES.get('event_image')
        if uploaded_image:
            max_upload_size = 500000
            if uploaded_image.size > max_upload_size:
                form.add_error('event_image',
                               "File size must not exceed 500KB.")

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
    ''' Display the votes a user has made based on authentication'''
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


class AdminSingleView(AdminRequiredMixin, View):
    """View SINGLE created VoteCard from the admin Dashboard."""
    template_name = 'backend/admin-dashboard/single_card_admin.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = VoteCard.objects.order_by('-created_on')
        event = get_object_or_404(queryset, slug=slug)
        candidates = event.candidates.all()

        # Progress bar
        now = timezone.now().date()
        total_duration = 0.01 + \
            (event.expire - event.created_on).days
        elapsed_time = (now - event.created_on).days
        event.progress = format(
            (elapsed_time / total_duration) * 100, '.0f')
        event.time_left = format(
            total_duration - elapsed_time, '.0f')

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
        if uploaded_image and validate_image_size(request, uploaded_image):
            event.event_image = uploaded_image

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
        if uploaded_image and validate_image_size(request, uploaded_image):
            event.event_image = uploaded_image

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

        # Check the image size here
        uploaded_image = request.FILES.get('event_image')
        if uploaded_image:
            max_upload_size = 500000
            if uploaded_image.size > max_upload_size:
                form.add_error('event_image',
                               "File size must not exceed 500KB.")

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
    """Return all system's votes with a status of 1,
    ordered by creation date."""
    model = VoteRecord
    template_name = 'backend/admin-dashboard/admin_votes.html'
    paginate_by = 10
    context_object_name = 'admin_votes'

    def get_queryset(self):
        return VoteRecord.objects.order_by('-timestamp')
