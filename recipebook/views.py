from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View 
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from .models import Entry, Rating, Contact
from .forms import CommentForm, RecipeForm


class EntryList(generic.ListView):
    model = Entry
    queryset = Entry.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3
 

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
                "comment_form": comment_form
            },
        )


class Recipes(generic.ListView):
    model = Entry
    queryset = Entry.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class AddRecipe(View):

    def get(self, request):
        context = {'recipe_form': RecipeForm()}
        return render(request, 'add_recipe.html', context)

    def post(self, request):
        if request.method == 'POST':
            recipe_form = RecipeForm(request.POST, initial={
                'author': request.user.email
            })
            if recipe_form.is_valid():
                recipe_form.instance.author = self.request.user
                recipe_form.instance.name = request.user.username
                recipe_form.instance.email = request.user.email
                recipe_form.save()
                messages.success(request, 'Your post will be visible upon approval.')
                return redirect('home')
            else:
                messages.error(request, "Your request couldn't be completed. Please try again.")
                context = {'recipe_form': recipe_form}
                return render(request, 'add_recipe.html', context)

        else:
            recipe_form = RecipeForm()

        context = {'recipe_form': recipe_form}
        return render(request, 'recipes.html', context)


class EditRecipe(UpdateView):
    model = Entry
    template_name = 'edit_recipe.html'
    form_class = RecipeForm
    success_url = 'recipes/'

    def recipe_form_valid(self, recipe_form):
        messages.success(self.request, 'Your modifications were saved successfully.')
        return super().recipe_form_valid(recipe_form)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('name')
        message = request.POST.get('message')
        query = Contact(name=name, email=email, message=message)
        query.save()
        messages.success('Your message is sent successfully!')
            
        return redirect('/contact')

    return render(request, 'contact.html')