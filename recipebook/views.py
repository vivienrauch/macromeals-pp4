from django.shortcuts import render
from django.views import generic
from .models import Entry


class EntryList(generic.ListView):
    model = Entry
    queryset = Post.objects.filter(status=1).order_by('-created-_on')
    template_name = 'index.html'
    paginate_by = 6
 