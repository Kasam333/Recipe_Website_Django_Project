# Generated by Django 5.1.4 on 2025-01-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_app', '0002_recipe_recipe_cook_time_recipe_recipe_prep_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Recipe_prep_time',
            field=models.CharField(max_length=10),
        ),
    ]
