# Generated by Django 3.2.19 on 2023-06-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0013_auto_20230609_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='Type your email here', max_length=254),
        ),
    ]
