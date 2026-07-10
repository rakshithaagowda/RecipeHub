from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category


def home(request):
    featured_recipes = Recipe.objects.filter(featured=True)[:6]
    categories = Category.objects.all()

    context = {
        "featured_recipes": featured_recipes,
        "categories": categories,
    }

    return render(request, "recipes/home.html", context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    context = {
        "recipe": recipe,
    }

    return render(request, "recipes/recipe_detail.html", context)