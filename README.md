A Django-based recipe website allowing users to browse, add, update, and manage their recipes. Users can also create profiles, upload profile and recipe images, and explore various cooking recipes with detailed instructions.

Features
User Authentication: Users can register, log in, and create profiles.
Recipe Management: Users can add new recipes, update existing ones, and view individual recipe details.
Image Upload: Supports uploading profile images and recipe images.
Recipe Categories: Categorize recipes for better organization.
Responsive Design: The website is designed to work on both desktop and mobile devices.




Kasam333-Recipe_Website_Project/
│
├── db.sqlite3                       # SQLite database
├── manage.py                         # Django's command-line utility
├── Base_app/                         # Main app for managing recipes and users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/                  # Database migrations
│   ├── __pycache__/                 # Compiled Python files
│
├── Media/                            # Directory for storing uploaded images
│   ├── profile_images/              # User profile images
│   └── recipe_images/               # Recipe images
│
├── Recipes_project/                 # Project settings and configurations
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/                
│
├── Static/                           # Static files (CSS, JS, images)
│   ├── css/
│   │   ├── account.css              # Styles for the account pages
│   │   ├── main.css                 # Main site styles
│   │   ├── normalize.css            # Normalize CSS
│   │   └── style.css                # Custom styles
│   ├── img/                          # Static images
│   └── js/
│       ├── app.js                   # Custom JavaScript
│       ├── bootstrap.js             # Bootstrap JS
│       └── custom.js                # Custom JavaScript for functionality
│
└── Templates/                        # HTML templates
    ├── about.html                   # About page template
    ├── account_base.html            # Base template for account pages
    ├── add_recipe.html              # Page for adding new recipes
    ├── base.html                    # Base template for all pages
    ├── home.html                    # Homepage template
    ├── login.html                   # Login page template
    ├── profile.html                 # User profile page template
    ├── recipes.html                 # Page displaying all recipes
    ├── register.html                # Registration page template
    ├── single_recipe.html           # Template for viewing individual recipe
    └── update_recipe.html           # Page for updating recipes

Prerequisites
Python 3.x
Django
SQLite (comes pre-configured with Django)

Installation
1. Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/Kasam333-Recipe_Website_Project.git
cd Kasam333-Recipe_Website_Project

2. Install dependencies:
bash
Copy code
pip install -r requirements.txt

3. Apply migrations:
bash
Copy code
python manage.py migrate

4. Run the development server:
bash
Copy code
python manage.py runserver
Now, open your browser and visit http://127.0.0.1:8000/ to access the website.

Usage
Register/Login: Create an account or log in to view and manage your recipes.
Add Recipe: Navigate to the "Add Recipe" page to submit a new recipe with details like ingredients, cook time, prep time, and images.
Browse Recipes: Browse through available recipes or search by category or ingredients.
Profile: Manage your account settings and view your personal recipes.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

License
This project is open-source and available under the MIT License.
