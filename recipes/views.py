from django.shortcuts import render
from .models import Recipe, Category


def home(request):
    featured_recipes = Recipe.objects.filter(featured=True)[:6]
    categories = Category.objects.all()

    context = {
        "featured_recipes": featured_recipes,
        "categories": categories,
    }

    return render(request, "recipes/home.html", context)