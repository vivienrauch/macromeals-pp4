from .models import Comment, Entry
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = (
            'featured_image',
            'title',
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