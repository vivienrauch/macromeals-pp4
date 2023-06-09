# Generated by Django 3.2.19 on 2023-06-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0012_auto_20230609_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='highest_in',
            field=models.CharField(choices=[('Protein', 'Protein'), ('Carbs', 'Carbs'), ('Fat', 'Fat'), ('-', '-')], default='-', max_length=25),
        ),
        migrations.AlterField(
            model_name='entry',
            name='lowest_in',
            field=models.CharField(choices=[('Protein', 'Protein'), ('Carbs', 'Carbs'), ('Fat', 'Fat'), ('-', '-')], default='-', max_length=25),
        ),
        migrations.AlterField(
            model_name='entry',
            name='meal_type',
            field=models.CharField(choices=[('Vegan', 'Vegan'), ('Vegetarian (lacto-ovo)', 'Vegetarian (lacto-ovo)'), ('Carnivore', 'Carnivore'), ('Pescitarian', 'Pescitarian'), ('-', '-')], default='-', max_length=25),
        ),
    ]
