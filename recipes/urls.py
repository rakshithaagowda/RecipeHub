from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Recipe Detail Page
    path("recipe/<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("ai-recipe/", views.ai_recipe, name="ai_recipe"),
    path("api/recipes/", views.api_recipes, name="api_recipes"),
    path("api/categories/", views.api_categories, name="api_categories"),
    path("api/recipes/<slug:slug>/", views.api_recipe_detail, name="api_recipe_detail"),
]