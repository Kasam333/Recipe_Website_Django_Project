from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Base_app.models import Recipe, UserProfile


# Utility function to handle profile image saving
def save_profile_image(profile_image, user_profile):
    if profile_image:
        fs = FileSystemStorage()
        filename = fs.save('profile_images/' + profile_image.name, profile_image)
        user_profile.profile_image = fs.url(filename)
        user_profile.save()

# View for user profile
@login_required
def user_profile(request):
    if request.method == 'POST' and request.FILES.get('profile_image'):
        profile_image = request.FILES['profile_image']
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        save_profile_image(profile_image, user_profile)
        messages.success(request, 'Profile image updated successfully.')
    return render(request, 'profile.html', {'user': request.user.userprofile})

# Registration view
def RegisterView(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        profile_image = request.FILES.get('profile_image')

        # Check if username exists
        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'Username is already taken')
            return redirect('/register/')

        # Create user and profile
        user = User.objects.create_user(username=user_name, email=email, password=password,
                                        first_name=first_name, last_name=last_name)
        user_profile = UserProfile.objects.create(user=user)

        # Handle profile image
        if profile_image:
            save_profile_image(profile_image, user_profile)

        messages.success(request, 'Account created successfully')
        return redirect('/')

    return render(request, "register.html")


# Login view
def LoginView(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/')

    return render(request, "login.html")


# Logout view
def logout_page(request):
    logout(request)
    return redirect('/')


# Home view displaying recipes
def HomeView(request):
    recipes = Recipe.objects.all()
    return render(request, "home.html", {'recipes': recipes})


# About view
def AboutView(request):
    return render(request, "about.html")


# Recipes view with search functionality
def RecipesView(request):
    search_query = request.GET.get('search', '')
    recipes = Recipe.objects.filter(Recipe_name__icontains=search_query) if search_query else Recipe.objects.all()
    return render(request, "recipes.html", {'recipes': recipes})


def SingleRecipeView(request,id):
    recipe = get_object_or_404(Recipe, id=id)

    return render(request, "single_recipe.html", {'recipe': recipe})


# Profile view displaying user's recipes
@login_required
def ProfileView(request):
    user = request.user
    search_query = request.GET.get('search', '')
    recipes = Recipe.objects.filter(User=user, Recipe_name__icontains=search_query) if search_query else Recipe.objects.filter(user=user)
    return render(request, "profile.html", {'recipes': recipes})


# Add recipe view
@login_required
def AddRecipeView(request):
    if request.method == 'POST':
        recipe_name = request.POST['recipe_name']
        recipe_description = request.POST['recipe_description']
        recipe_ingridients = request.POST['recipe_ingridients']
        recipe_steps = request.POST['recipe_steps']
        recipe_prep_time = request.POST['recipe_preparation_time']
        recipe_cook_time = request.POST['recipe_cook_time']
        recipe_yt_url = request.POST['recipe_yt_link']
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            user=request.user,
            Recipe_name=recipe_name,
            Recipe_description=recipe_description,
            Recipe_ingridients=recipe_ingridients,
            Recipe_steps=recipe_steps,
            Recipe_prep_time=recipe_prep_time,
            Recipe_cook_time=recipe_cook_time,
            Recipe_yt_url=recipe_yt_url,
            Recipe_image=recipe_image
        )

        messages.success(request, 'Recipe added successfully')
        return redirect('/add-recipe/')

    return render(request, "add_recipe.html")


# Update recipe view
@login_required
def UpdateRecipeView(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        recipe.Recipe_name = request.POST['recipe_name']
        recipe.Recipe_description = request.POST['recipe_description']
        recipe.Recipe_ingridients = request.POST['recipe_ingridients']
        recipe.Recipe_steps = request.POST['recipe_steps']
        recipe.Recipe_prep_time = request.POST['recipe_preparation_time']
        recipe.Recipe_cook_time = request.POST['recipe_cook_time']
        recipe.Recipe_yt_url = request.POST['recipe_yt_link']

        recipe_image = request.FILES.get('recipe_image')
        if recipe_image:
            recipe.Recipe_image = recipe_image

        recipe.save()
        messages.success(request, 'Recipe updated successfully.')
        return redirect('/profile/')

    return render(request, "update_recipe.html", {'recipe': recipe})


# Delete recipe view
@login_required
def DeleteRecipeView(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    messages.success(request, 'Recipe deleted successfully.')
    return redirect('/profile/')
