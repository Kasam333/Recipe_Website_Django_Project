# Generated by Django 5.1.4 on 2025-01-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_app', '0007_remove_recipe_recipe_ingridients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe_steps',
            name='recipe',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='User',
            new_name='user',
        ),
        migrations.AddField(
            model_name='recipe',
            name='Recipe_ingridients',
            field=models.TextField(default='Not specified'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='Recipe_steps',
            field=models.TextField(default='Not specified'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Recipe_Steps',
        ),
    ]
