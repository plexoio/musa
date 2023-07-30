from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic
from musa.models import UserProfile
from django.shortcuts import get_object_or_404, redirect
from django import forms
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse


class UserRequiredMixin(UserPassesTestMixin):
    """Mixin to check user roles for access control (either role 0 or 1)."""

    def test_func(self):
        user_profile = self.request.user
        return user_profile.is_authenticated and (
            user_profile.role in [0, 1])


class UserDashboard(UserRequiredMixin, generic.DetailView):
    """Display the dashboard for regular users."""
    model = UserProfile
    template_name = 'backend/user-dashboard/index.html'
    context_object_name = 'user_dashboard'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the context
        context = super().get_context_data(**kwargs)
        # Add the VoteCard instances to the context
        user_profile = self.get_object()
        context['vote_cards'] = user_profile.user_card.all()
        print(user_profile.user_card.all())
        return context


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
