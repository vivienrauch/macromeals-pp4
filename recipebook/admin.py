from django.contrib import admin
from .models import Entry, Comment, Rating
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Entry)
class EntryAdmin(SummernoteModelAdmin):

    list_display = (
        'title',
        'slug',
        'status',
        'created_on',
        'highest_in',
        'lowest_in',
        'meal_type'
        )
    search_fields = (
        'title',
        'cooking_time',
        'protein',
        'carbs',
        'fat',
        'highest_in',
        'lowest_in',
        'meal_type')

    prepopulated_fields = {'slug': ('title',)}
    list_filter = (
        'status',
        'created_on',
        'highest_in',
        'lowest_in',
        'meal_type'
        )
    summernote_fields = ('steps', 'ingredients')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'entry', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email address', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ('user', 'entry', 'rating')
