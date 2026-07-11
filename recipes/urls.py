from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Recipe Detail Page
    path("recipe/<slug:slug>/", views.recipe_detail, name="recipe_detail"),
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
]