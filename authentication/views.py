from allauth.account.views import LoginView, SignupView, LogoutView
from musa.forms import CustomSignupForm, CustomLoginForm
from django.urls import reverse_lazy, reverse

# LOGIN, SIGUNUP & LOGOUT


class CustomLoginView(LoginView):
    """Custom login view that redirects users to  dashboard after login."""
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
