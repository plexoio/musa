from django.contrib.auth.views import PasswordChangeView
from allauth.account.views import LoginView, SignupView, LogoutView
from django.views import View, generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import VoteCard, UserProfile, VoteRecord
from django import forms
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from .forms import CustomSignupForm, CustomLoginForm, VoteCardCreationForm
from django.http import HttpResponseBadRequest
from django.shortcuts import render

# GENERAL


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

# LOGIN, SIGUNUP & LOGOUT


class CustomLoginView(LoginView):
    """Custom login view that redirects users to their dashboard after login."""
    form_class = CustomLoginForm
    template_name = 'account/login.html'

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy('user_dashboard', kwargs={'pk': user_id})


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'


class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html'

# USER


class UserRequiredMixin(UserPassesTestMixin):
    """Mixin to check user roles for access control (either role 0 or 1)."""

    def test_func(self):
        user_profile = self.request.user
        return user_profile.is_authenticated and (
            user_profile.role in [0, 1])


class UserDashboard(UserRequiredMixin, LoginRequiredMixin, generic.DetailView):
    """Display the dashboard for regular users."""
    model = UserProfile
    template_name = 'backend/user-dashboard/index.html'
    context_object_name = 'user_dashboard'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, pk=self.request.user.pk)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email']


class UserSettings(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'backend/user-dashboard/settings.html'
    context_object_name = 'user_settings'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user_settings')


class UserDelete(UserRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'backend/user-dashboard/user_delete.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        # Redirect to login after deletion
        return reverse_lazy('account_login')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)

        # Log the user out after deletion
        logout(request)

        return response


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']


class UserPasswordChangeView(UserRequiredMixin, PasswordChangeView):
    template_name = 'backend/user-dashboard/password_change.html'
    form_class = UserPasswordChangeForm
    context_object_name = 'user_change'

    def get_success_url(self):
        return reverse('user_settings')

# USER Event Management

# CREATE Event


class VoteCardCreation(View):
    template_name = 'backend/user-dashboard/create.html'

    def get(self, request, *args, **kwargs):
        form = VoteCardCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = VoteCardCreationForm(request.POST, request.FILES)
        if form.is_valid():
            vote_card = form.save(commit=False)
            vote_card.author = request.user
            vote_card.save()
            return redirect('user_dashboard')
        else:
            # Return a bad request response or render the form with errors
            return HttpResponseBadRequest("Invalid form data")

# ADMIN


class AdminRequiredMixin(UserPassesTestMixin):
    """Mixin to check for admin role (role 2) for access control."""

    def test_func(self):
        user_profile = self.request.user
        return user_profile and user_profile.role == 2


class AdminDashboard(AdminRequiredMixin, LoginRequiredMixin, generic.DetailView):
    """Display the dashboard for admins."""
    model = UserProfile
    template_name = 'backend/admin-dashboard/index.html'
    context_object_name = 'admin_dashboard'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, pk=self.request.user.pk)


class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'username']


class AdminSettings(UpdateView):
    model = UserProfile
    form_class = AdminProfileForm
    template_name = 'backend/admin-dashboard/settings.html'
    context_object_name = 'admin_settings'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('admin_settings')


class AdminPasswordChangeForm(PasswordChangeForm):
    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']


class AdminPasswordChangeView(AdminRequiredMixin, PasswordChangeView):
    template_name = 'backend/admin-dashboard/password_change.html'
    form_class = AdminPasswordChangeForm
    context_object_name = 'admin_change'

    def get_success_url(self):
        return reverse('admin_settings')

# HOMEPAGE


class HomePage(BaseListView):
    """Frontend main page displaying the list of VoteCards."""
    template_name = 'frontend/index.html'
    context_object_name = 'home_page'
