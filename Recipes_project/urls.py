"""
URL configuration for Recipes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Base_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterView, name= "Register"),
    path('',LoginView, name="Login"),
    path('home/',HomeView,name='Home'),
    path('about/',AboutView,name='About'),
    path('recipes/',RecipesView,name='Recipes'),
    path('single-recipe/<int:id>/',SingleRecipeView, name='SingleRecipe'),
    path('profile/',ProfileView,name='Profile'),
    path('add-recipe/',AddRecipeView,name='AddRecipe'),
    path('update-recipe/<int:id>/', UpdateRecipeView, name='UpdateRecipe'),
    path('delete-recipe/<int:id>/', DeleteRecipeView, name='DeleteRecipe'),
    path('logout/',logout_page,name='Logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
