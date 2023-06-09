from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))

# High variables
high_protein = "Protein"
high_carb = "Carbs"
high_fat = "Fat"
empty_field = "-"
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
vegan = "Vegan"
carnivore = "Carnivore"
vegetarian = "Vegetarian (lacto-ovo)"
pescitarian = "Pescitarian"
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
    ingredients = models.TextField(blank=False)
    steps = models.TextField(blank=False)
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
        max_length = 25,
        choices = macro_high_choices,
        default = empty_field
        ) 
    lowest_in = models.CharField(
        max_length = 25,
        choices = macro_low_choices,
        default = empty_field
    )
    meal_type = models.CharField(
        max_length = 25,
        choices = meal_type_choices,
        default = empty_field
    )

    class Meta:
        ordering = ['-created_on']

    # inspired by the following source:
    # https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c

    def average_rating(self) -> float:
        return Rating.objects.filter(entry=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.title}: {self.average_rating()}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'slug': self.slug})


class Rating(models.Model):
    """
    Storing the Rating data
    """
    entry = models.ForeignKey(Entry, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(User, default=0)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.entry.title}: {self.rating}"


class Comment(models.Model):
    """
    Storing the Comment data
    """
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
    """
    Storing the Contact data
    """
    name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, default='Type your email here')
    message = models.TextField(blank=False, default='Type your question/recipe here:')

    def __str__(self):
        return f"{self.name} sent a message from {self.email}"