# Django Imports
from django.db import models
from django.utils import timezone

# Library Imports
from cloudinary.models import CloudinaryField

STATUS = (
    (0, 'Draft'),
    (1, 'Online'),
    (2, 'Cancelled'),
    (3, 'Completed')
)

CARD_TYPE = (
    (0, 'Community'),
    (1, 'Official')
)


class Category(models.Model):
    """Model representing a voting category, like "Best Artist"."""
    category_name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['category_name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class VoteCard(models.Model):
    """Model representing a card where users can cast their votes."""
    title = models.CharField(max_length=33, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        'musa.UserProfile', on_delete=models.CASCADE,
        related_name="card_author")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories")
    mission = models.CharField(max_length=33)
    location = models.CharField(max_length=33)
    description = models.TextField(max_length=258)
    expire = models.DateField()
    event_image = CloudinaryField('image',
                                  default='placeholder')
    vote_record = models.ManyToManyField('musa.UserProfile',
                                         through='VoteRecord',
                                         related_name='user_votes', blank=True)
    candidates = models.ManyToManyField('ElectedPerson',
                                        related_name='vote_cards',
                                        blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    type = models.IntegerField(choices=CARD_TYPE, default=0)
    created_on = models.DateField(auto_now_add=True)

    def is_expired(self):
        expired = self.expire <= timezone.now().date()
        return expired

    def update_card(self):
        if self.is_expired() and self.status != 3:
            self.status = 3
            self.save()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_votes(self):
        """Return the count of votes."""
        return self.vote_record.count()


class VoteRecord(models.Model):
    """Model representing the record of a single vote by a user."""
    voter = models.ForeignKey(
        'musa.UserProfile', on_delete=models.CASCADE,
        related_name="voter_record")
    vote_card = models.ForeignKey(  # consider renaming in the future
        VoteCard, on_delete=models.CASCADE, related_name="votecard_record")
    elected_person = models.ForeignKey('ElectedPerson',
                                       on_delete=models.CASCADE,
                                       related_name="elected_record")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.elected_person.name


class ElectedPerson(models.Model):
    """Model representing a person who can be elected in a vote.
    'name' can be False in the future if necessary"""
    name = models.CharField(max_length=80, unique=True)
    is_elected = models.BooleanField(default=False)
    vote_card = models.ForeignKey(  # consider renaming in the future
        VoteCard, on_delete=models.CASCADE,
        related_name="vote_candidate", blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
