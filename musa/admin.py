from django.contrib import admin
from .models import UserProfile
from vote_management.models import Category, VoteCard, VoteRecord, ElectedPerson
from django_summernote.admin import SummernoteModelAdmin


@admin.register(VoteCard)
class VoteCardAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['description', 'title']
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    summernote_fields = 'description'


admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(VoteRecord)
admin.site.register(ElectedPerson)
