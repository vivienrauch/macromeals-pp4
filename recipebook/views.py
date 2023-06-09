from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from .models import Entry, Rating, Contact
from .forms import CommentForm, RecipeForm


class EntryList(generic.ListView):
    """
    The main page where 3 of the recipes
    are rendered at once.
    """
    model = Entry
    queryset = Entry.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class EntryDetail(View):
    """
    Based on the "I think therefore I blog" walkthrough project.
    It renders each individual post the user clicks on.
    If the user is logged in, they are able to rate and comment.
    The comment will need to be approved by the admin.
    """
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

            user_rating = request.POST.get("rating")
            if user_rating:
                rating = int(user_rating)
            Rating.objects.create(
                entry=entry, user=request.user, rating=rating
            )

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
                "comment_form": comment_form,
            },
        )


class Recipes(generic.ListView):
    """
    A page where all the recipes are rendered,
    6 recipes displayed per page.
    """
    model = Entry
    queryset = Entry.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


def AddRecipe(request):
    """
    Allows the user to add their own recipes.
    """
    recipe_form = RecipeForm(request.POST or None, request.FILES or None)
    context = {
        'recipe_form': recipe_form,
    }

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form.instance.author = request.user
            recipe_form.instance.status = 1
            recipe = recipe_form.save(commit=False)

            recipe.save()
            messages.success(request, 'Your recipe was saved successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong. Please try again.')
    else:
        recipe_form = RecipeForm()
    return render(request, 'add_recipe.html', context)


class EditRecipe(UpdateView):
    """
    Allows the user to edit the recipe of which
    they are the author.
    """
    model = Entry
    template_name = 'edit_recipe.html'
    form_class = RecipeForm


class DeleteRecipe(DeleteView):
    """
    Allows the user to delete the recipe of which
    they are the author.
    """
    model = Entry
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('recipes')


def contact(request):
    """
    A contact page where both registered and
    unregistered users can send their recipes and
    questions.
    If the message will be successfully sent,
    it will redirect the user back to the contact page.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        query = Contact(name=name, email=email, message=message)
        query.save()
        messages.success(request, 'Your message is sent successfully!')

        return redirect('/contact')

    return render(request, 'contact.html')
