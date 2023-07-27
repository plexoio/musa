from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


STATUS = (
    (0, 'Draft'),
    (1, 'Published'),
    (3, 'Disapproved')
)

ROLES = (
    (0, 'User'),
    (1, 'Publisher'),
    (2, 'Admin')
)


class Category(models.Model):
    """Model representing a voting category, like "Best Artist"."""
    category_name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['category_name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class UserProfile(AbstractUser):
    """Extended user profile with custom attributes."""
    verified = models.BooleanField(default=False)
    role = models.IntegerField(choices=ROLES, default=0)
    vote_records = models.ManyToManyField(
        'VoteCard', through='VoteRecord', related_name='vote_records')

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class VoteCard(models.Model):
    """Model representing a card where users can cast their votes."""
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="vote_cards")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories")
    mission = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    description = models.TextField(max_length=400)
    expire = models.DateField(auto_now_add=True)
    event_image = CloudinaryField('image', default='placeholder')
    vote_record = models.ManyToManyField(
        UserProfile, through='VoteRecord', related_name='user_votes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_votes(self):
        """Return the count of votes."""
        return self.vote_record.count()


class VoteRecord(models.Model):
    """Model representing the record of a single vote by a user."""
    voter = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    vote_card = models.ForeignKey(
        VoteCard, on_delete=models.PROTECT, related_name="votecard_record")
    elected_person = models.ForeignKey(
        'ElectedPerson', on_delete=models.PROTECT, related_name="elected_record")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.elected_person.name


class ElectedPerson(models.Model):
    """Model representing a person who can be elected in a vote."""
    name = models.CharField(max_length=80, unique=True)
    is_elected = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
