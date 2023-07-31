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


# ADMIN

class AdminRequiredMixin(UserPassesTestMixin):
    """Mixin to check for admin role (role 2) for access control."""

    def test_func(self):
        user_profile = self.request.user
        return user_profile and user_profile.role == 2


class AdminDashboard(AdminRequiredMixin, generic.DetailView):
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


class AdminSettings(AdminRequiredMixin, UpdateView):
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