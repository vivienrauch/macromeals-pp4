# Generated by Django 3.2.19 on 2023-05-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='carbs',
            field=models.IntegerField(default=0, help_text='Add your carbs in grams'),
        ),
        migrations.AddField(
            model_name='entry',
            name='fat',
            field=models.IntegerField(default=0, help_text='Add your fats in grams'),
        ),
        migrations.AddField(
            model_name='entry',
            name='kcal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='protein',
            field=models.IntegerField(default=0, help_text='Add your protein in grams'),
        ),
    ]