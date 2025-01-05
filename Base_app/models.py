from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Recipe_name = models.CharField(max_length=100)
    Recipe_description = models.TextField()
    Recipe_ingridients = models.TextField(default='Not specified')
    Recipe_steps = models.TextField(default='Not specified')
    Recipe_prep_time = models.CharField(max_length=10)
    Recipe_cook_time = models.CharField(max_length=10, default='00:00')
    Recipe_yt_url = models.URLField(blank=True)
    Recipe_image = models.ImageField(upload_to='recipe_images/', blank=False)

    def __str__(self):
        return self.Recipe_name