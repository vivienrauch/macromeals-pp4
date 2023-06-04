from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Entry
from .forms import CommentForm


class EntryList(generic.ListView):
    model = Entry
    queryset = Entry.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
 

class EntryDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Entry.objects.filter(status=1)
        entry = get_object_or_404(queryset, slug=slug)
        comments = entry.comments.filter(approved=True).order_by('created_on')
        rating = entry.average_rating

        return render(
            request,
            "entry_detail.html",
            {
                "entry": entry,
                "comments": comments,
                "commented": False,
                "rating": rating,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Entry.objects.filter(status=1)
        entry = get_object_or_404(queryset, slug=slug)
        comments = entry.comments.filter(approved=True).order_by('created_on')
        rating = entry.average_rating

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.entry = entry
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "entry_detail.html",
            {
                "entry": entry,
                "comments": comments,
                "commented": True,
                "rating": rating,
                "comment_form": comment_form
            },
        )


