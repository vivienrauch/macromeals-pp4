from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Entry(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    cooking_time = models.IntegerField(
        default=0, 
        help_text = "Add your cooking/preparation time in minutes"
        )
    ingredients = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    kcal = models.IntegerField(default=0)
    protein = models.IntegerField(help_text = "Add your protein in grams", default=0)
    carbs = models.IntegerField(help_text = "Add your carbs in grams", default=0)
    fat = models.IntegerField(help_text = "Add your fats in grams", default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    high_protein = "HP"
    high_carb = "HC"
    high_fat = "HF"
    empty_field = "EF"
    macro_high_choices = [
        (high_protein, "Protein"),
        (high_carb, "Carbs"),
        (high_fat, "Fat"),
        (empty_field, "-")
        ]
    highest_in = models.CharField(
        max_length = 2,
        choices = macro_high_choices,
        default = empty_field
        )
    low_protein = "LP"
    low_carb = "LC"
    low_fat = "LF"
    macro_low_choices = [
        (low_protein, "Protein"),
        (low_carb, "Carbs"),
        (low_fat, "Fat"),
        (empty_field, "-")
    ]
    lowest_in = models.CharField(
        max_length = 2,
        choices = macro_low_choices,
        default = empty_field
    )
    vegan = 'VE'
    carnivore = 'CA'
    vegetarian = 'LO'
    pescitarian = 'PE'
    meal_type_choices = [
        (vegan, "Vegan"),
        (vegetarian, "Vegetarian (lacto-ovo)"),
        (carnivore, "Carnivore"),
        (pescitarian, "Pescitarian"),
        (empty_field, "-")
    ]
    meal_type = models.CharField(
        max_length = 2,
        choices = meal_type_choices,
        default = empty_field
    )


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


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
    