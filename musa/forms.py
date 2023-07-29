from cloudinary.forms import CloudinaryFileField
from .models import VoteCard, UserProfile, Category, ElectedPerson
from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.utils.text import slugify


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

# CREATE Event


class VoteCardCreationForm(forms.ModelForm):
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

    def save(self, commit=True):
        instance = super(VoteCardCreationForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance

    class Meta:
        model = VoteCard
        fields = [
            'title', 'author', 'category', 'mission',
            'location', 'description', 'expire', 'event_image', 'candidates'
        ]

        widgets = {
            'expire': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }

        labels = {
            'title': 'Event Title',
            'author': 'Event Author',
            'category': 'Event Category',
        }

        help_texts = {
            'title': 'Enter the title for the event. Must be unique.',
            'expire': 'Enter the date the event will expire.',
            'description': 'Enter a catchy description',
            'location': 'Enter your target location'
        }


class ElectedPersonForm(forms.ModelForm):
    class Meta:
        model = ElectedPerson
        fields = '__all__'
