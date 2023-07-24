from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, 'Draft'),
    (1, 'Published'),
    (3, 'Disapproved')
)

ROLES = (
    (0, 'User'),
    (1, 'Publisher'),
)


# Category Model


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

# User Extended


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    role = models.IntegerField(choices=ROLES, default=0)
    vote_records = models.ManyToManyField(
        'VoteCard', through='VoteRecord', related_name='vote_records')

    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return self.user.username

# VoteCard Model


class VoteCard(models.Model):
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
        return self.vote_record.count()

# VoteRecord model


class VoteRecord(models.Model):
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


# ElectedPerson


class ElectedPerson(models.Model):
    name = models.CharField(max_length=80, unique=True)
    is_elected = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
