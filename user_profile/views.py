# Django imports
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View, generic
from django.views.generic.edit import UpdateView, DeleteView
from django import forms
from django.core.exceptions import PermissionDenied

# Local imports
from musa.models import UserProfile


class UserRequiredMixin(UserPassesTestMixin):
    """Mixin to check user roles for access control (either role 0 or 1)."""

    def test_func(self):
        user_profile = self.request.user
        return user_profile.is_authenticated and (
            user_profile.role in [0, 1]
        )


class UserDashboard(UserRequiredMixin, generic.DetailView):
    """Display the dashboard for regular users."""
    model = UserProfile
    template_name = 'backend/user-dashboard/index.html'
    context_object_name = 'user_dashboard'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = self.get_object()
        context['vote_cards'] = user_profile.user_card.order_by(
            '-created_on').all()
        return context


class UserProfileForm(forms.ModelForm):
    """Form for updating user profile."""

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email']

# UPDATE


class UserSettings(UpdateView):
    """View for updating user settings."""
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'backend/user-dashboard/settings.html'
    context_object_name = 'user_settings'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user_settings')

# DELETE


class UserDelete(UserRequiredMixin, DeleteView):
    """View for deleting the user profile."""
    model = UserProfile
    template_name = 'backend/user-dashboard/user_delete.html'

    allowed_roles = [0]

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.user_votes.all():
            raise PermissionDenied(
                "You do not have permission to delete your account.")
        elif user.card_author.all():
            raise PermissionDenied(
                "You do not have permission to delete your account.")
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('account_login')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        logout(request)
        return response


class UserPasswordChangeForm(PasswordChangeForm):
    """Form for changing the user's password."""

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']


class UserPasswordChangeView(UserRequiredMixin, PasswordChangeView):
    """View for changing the user's password."""
    template_name = 'backend/user-dashboard/password_change.html'
    form_class = UserPasswordChangeForm
    context_object_name = 'user_change'

    def get_success_url(self):
        return reverse('user_settings')

# ROLE


class UserRole(UserDashboard):
    template_name = 'backend/user-dashboard/role.html'
