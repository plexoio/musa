# Django Imports
from django import forms
from django.utils.text import slugify

# Python imports
from datetime import date

# Library Imports
from allauth.account.forms import LoginForm, SignupForm
from cloudinary.forms import CloudinaryFileField

# Local Imports
from .models import UserProfile
from vote_management.models import VoteCard, Category, ElectedPerson


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, label='First Name', required=True)
    last_name = forms.CharField(
        max_length=30, label='Last Name', required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


CustomLoginForm = LoginForm

# USER Create Event Form


class UserVoteCardCreationForm(forms.ModelForm):
    event_image = CloudinaryFileField(
        options={
            'crop': 'scale',
            'width': 400,
            'height': 300,
        },
        required=False
    )

    candidates = forms.ModelMultipleChoiceField(
        queryset=ElectedPerson.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def clean_expire(self):
        expire_date = self.cleaned_data.get('expire')
        if expire_date and expire_date < date.today():
            raise forms.ValidationError(
                "The expiration date cannot be in the past.")
        return expire_date

    def save(self, commit=True):
        instance = super(UserVoteCardCreationForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = VoteCard
        fields = [
            'title', 'author', 'category', 'mission',
            'location', 'description', 'expire',
            'event_image', 'candidates', 'type'
        ]

        widgets = {
            'expire': forms.DateInput(attrs={'type': 'date', 'min': date.today(
            )}),
            'description': forms.Textarea(attrs={'rows': 4, 'maxlength': 264}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }

        labels = {
            'title': 'Title',
            'author': 'Author',
            'category': 'Category',
            'mission': 'Mission',
            'type': 'Type',
            'event_image': 'Image'
        }

        help_texts = {
            'title': 'Enter a unique & descriptive the title for the event.',
            'expire': 'Enter the date the event will expire.',
            'description': 'Enter a catchy description',
            'location': 'Enter your target location',
            'mission': 'State clearly your mission',
            'author': 'You are currently the author of this event',
            'event_image': 'File size cannot exceed 500 KB'
        }

# ADMIN Create Event Form


class AdminVoteCardCreationForm(forms.ModelForm):
    event_image = CloudinaryFileField(
        options={
            'crop': 'scale',
            'width': 400,
            'height': 300,
        },
        required=False
    )

    candidates = forms.ModelMultipleChoiceField(
        queryset=ElectedPerson.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def clean_expire(self):
        expire_date = self.cleaned_data.get('expire')
        if expire_date and expire_date < date.today():
            raise forms.ValidationError(
                "The expiration date cannot be in the past.")
        return expire_date

    def save(self, commit=True):
        instance = super(AdminVoteCardCreationForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = VoteCard
        fields = [
            'title', 'author', 'category', 'mission',
            'location', 'description', 'expire',
            'event_image', 'candidates', 'status', 'type'
        ]

        widgets = {
            'expire': forms.DateInput(attrs={'type': 'date', 'min': date.today(
            )}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }

        labels = {
            'title': 'Title',
            'author': 'Author',
            'category': 'Category',
            'mission': 'Mission',
            'type': 'Type',
            'event_image': 'Image'

        }

        help_texts = {
            'title': 'Enter a unique & descriptive the title for the event.',
            'expire': 'Enter the date the event will expire.',
            'description': 'Enter a catchy description',
            'location': 'Enter your target location',
            'mission': 'State clearly your mission',
            'author': 'You are currently the author of this event',
            'event_image': 'File size cannot exceed 500 KB'
        }


class ElectedPersonForm(forms.ModelForm):

    class Meta:
        model = ElectedPerson
        fields = '__all__'
