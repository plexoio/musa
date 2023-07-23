from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft')), (1, 'Published')

# VoteCard Model


class VoteCard(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="vote_cards")
    category = models.ForeignKey(
        category, on_delete=models.CASCADE, related_name="categories")
    mission = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    description = models.TextField(max_length=400)
    expire = models.DateField(auto_now=True)
    event_image = CloudinaryField('image', default='placeholder')
    vote_record = models.ManyToManyField(
        User, through='VoteRecord', related_name='user_votes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return self.title

        def number_of_votes(self):
            return self.vote_record.count()
