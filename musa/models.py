# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    (0, 'User'),
    (1, 'Publisher'),
    (2, 'Admin')
)


class UserProfile(AbstractUser):
    """Extended user profile with custom attributes."""
    verified = models.BooleanField(default=False)
    role = models.IntegerField(choices=ROLES, default=0)
    user_card = models.ManyToManyField(
        'vote_management.VoteCard',
        through='vote_management.VoteRecord', related_name='user_cards')

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username
