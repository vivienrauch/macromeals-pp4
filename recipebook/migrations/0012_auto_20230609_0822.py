# Generated by Django 3.2.19 on 2023-06-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0011_auto_20230607_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='highest_in',
            field=models.CharField(choices=[('Protein', 'Protein'), ('Carbs', 'Carbs'), ('Fat', 'Fat'), ('-', '-')], default='-', max_length=8),
        ),
        migrations.AlterField(
            model_name='entry',
            name='lowest_in',
            field=models.CharField(choices=[('Protein', 'Protein'), ('Carbs', 'Carbs'), ('Fat', 'Fat'), ('-', '-')], default='-', max_length=8),
        ),
        migrations.AlterField(
            model_name='entry',
            name='meal_type',
            field=models.CharField(choices=[('Vegan', 'Vegan'), ('Vegetarian (lacto-ovo)', 'Vegetarian (lacto-ovo)'), ('Carnivore', 'Carnivore'), ('Pescitarian', 'Pescitarian'), ('-', '-')], default='-', max_length=23),
        ),
    ]
