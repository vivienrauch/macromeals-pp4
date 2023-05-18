from django.contrib import admin
from .models import Entry
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Entry)
class EntryAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('content')
