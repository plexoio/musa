# Django Imports
from django.shortcuts import redirect
from django.views import View


class RoleRedirectView(View):
    '''' Redirect based on the user's role '''

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.role == 0:
            return redirect('/user/')
        elif user.role == 1:
            return redirect('/user/')
        elif user.role == 2:
            return redirect('/office/')
        else:
            return redirect('/user/')
