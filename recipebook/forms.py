from .models import Comment, Entry, Contact
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    The class uses the Comment model
    and displays the body field on the form.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Uses the Entry model with
    field specification.
    """
    class Meta:
        model = Entry
        fields = (
            'featured_image',
            'title',
            'excerpt',
            'cooking_time',
            'ingredients',
            'steps',
            'kcal',
            'protein',
            'carbs',
            'fat',
            'highest_in',
            'lowest_in',
            'meal_type',
        )

        widgets = {
            'ingredients': SummernoteWidget(),
            'steps': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)



        