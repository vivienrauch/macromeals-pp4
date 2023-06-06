from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))

# High variables
high_protein = "Protein"
high_carb = "Carbs"
high_fat = "Fat"
empty_field = "EF"
macro_high_choices = [
    (high_protein, "Protein"),
    (high_carb, "Carbs"),
    (high_fat, "Fat"),
    (empty_field, "-")
    ]

# Low variables
low_protein = "Protein"
low_carb = "Carbs"
low_fat = "Fat"
macro_low_choices = [
    (low_protein, "Protein"),
    (low_carb, "Carbs"),
    (low_fat, "Fat"),
    (empty_field, "-")
    ]

# Meal type variables
vegan = 'Vegan'
carnivore = 'Carnivore'
vegetarian = 'Vegetarian (lacto-ovo)'
pescitarian = 'Pescitarian'
meal_type_choices = [
    (vegan, "Vegan"),
    (vegetarian, "Vegetarian (lacto-ovo)"),
    (carnivore, "Carnivore"),
    (pescitarian, "Pescitarian"),
    (empty_field, "-")
    ]


class Entry(models.Model):
    """
    Storing Entry data
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    cooking_time = models.IntegerField(
        default=0, 
        help_text = "Add your cooking time in minutes"
        )
    ingredients = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    kcal = models.IntegerField(default=0)
    protein = models.IntegerField(
        help_text = "Add your amount in grams", default=0
        )
    carbs = models.IntegerField(help_text = "Add your amount in grams", default=0)
    fat = models.IntegerField(help_text = "Add your amount in grams", default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    highest_in = models.CharField(
        max_length = 8,
        choices = macro_high_choices,
        default = empty_field
        ) 
    lowest_in = models.CharField(
        max_length = 8,
        choices = macro_low_choices,
        default = empty_field
    )
    meal_type = models.CharField(
        max_length = 23,
        choices = meal_type_choices,
        default = empty_field
    )

    class Meta:
        ordering = ['-created_on']

    def number_of_likes(self):
        return self.likes.count()

    # inspired by the following source:
    # https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c

    def average_rating(self) -> float:
        return Rating.objects.filter(entry=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.title}: {self.average_rating()}"


class Rating(models.Model):
    entry = models.ForeignKey(Entry, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(User, default=0)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.entry.title}: {self.rating}"


class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=80, blank=False, null=False)
    message = models.TextField(blank=False, null=False, default="Type your question/recipe here:")

    def get_absolute_url(self):
        return reverse("contact", kwargs={"pk": self.pk}) 
    