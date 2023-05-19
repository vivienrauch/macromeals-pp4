from django.contrib import admin
from .models import Entry
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Entry)
class EntryAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content', 'protein', 'carbs', 'fat')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
