from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Entry(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    kcal = models.IntegerField(default=0)
    protein = models.IntegerField(help_text = "Add your protein in grams", default=0)
    carbs = models.IntegerField(help_text = "Add your carbs in grams", default=0)
    fat = models.IntegerField(help_text = "Add your fats in grams", default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class HighInMacro(models.Model):
    high_protein = "HP"
    high_carb = "HC"
    high_fat = "HF"
    macro_high_choices = [
        (high_protein, "High in protein"),
        (high_carb, "High in carbs"),
        (high_fat, "High in fat")
    ]
    macro_high = models.CharField(
        max_length = 2,
        choices = macro_high_choices,
    )


class LowInMacro(models.Model):
    low_protein = "LP"
    low_carb = "LC"
    low_fat = "LF"
    macro_low_choices = [
        (low_protein, "Low in protein"),
        (low_carb, "Low in carbs"),
        (low_fat, "Low in fat")
    ]
    macro_low = models.CharField(
        max_length = 2,
        choices = macro_low_choices,
    )


class ModerateInMacro(models.Model):
    moderate_protein = "MP"
    moderate_carb = "MC"
    moderate_fat = "MF"
    macro_moderate_choices = [
        (moderate_protein, "Moderate in protein"),
        (moderate_carb, "Moderate in carbs"),
        (moderate_fat, "Moderate in fat")
    ]
    macro_moderate = models.CharField(
        max_length = 2,
        choices = macro_moderate_choices,
    )


class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    