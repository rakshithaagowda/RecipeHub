from django.shortcuts import render, get_object_or_404

from .models import Recipe, Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .gemini_service import generate_recipe
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RecipeSerializer, CategorySerializer


def home(request):
    query = request.GET.get("q", "")

    featured_recipes = Recipe.objects.filter(featured=True)[:6]
    categories = Category.objects.all()

    search_results = None

    if query:
        search_results = Recipe.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query)
        )

    context = {
        "featured_recipes": featured_recipes,
        "categories": categories,
        "query": query,
        "search_results": search_results,
    }

    return render(request, "recipes/home.html", context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    related_recipes = Recipe.objects.filter(
        category=recipe.category
    ).exclude(id=recipe.id)[:3]

    context = {
        "recipe": recipe,
        "related_recipes": related_recipes,
    }

    return render(request, "recipes/recipe_detail.html", context)

    
def recipe_list(request):
    recipe_list = Recipe.objects.all()

    categories = Category.objects.all()

    category_slug = request.GET.get("category")
    difficulty = request.GET.get("difficulty")

    if category_slug:
        recipe_list = recipe_list.filter(category__slug=category_slug)

    if difficulty:
        recipe_list = recipe_list.filter(difficulty=difficulty)

    paginator = Paginator(recipe_list, 6)

    page_number = request.GET.get("page")
    recipes = paginator.get_page(page_number)

    context = {
        "recipes": recipes,
        "categories": categories,
        "selected_category": category_slug,
        "selected_difficulty": difficulty,
    }

    return render(request, "recipes/recipe_list.html", context)
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)

    recipes = Recipe.objects.filter(category=category)

    context = {
        "category": category,
        "recipes": recipes,
    }

    return render(
        request,
        "recipes/category_detail.html",
        context
    )
def ai_recipe(request):

    recipe = None
    ingredients = ""

    if request.method == "POST":

        ingredients = request.POST.get("ingredients")

    if ingredients:

        recipe = generate_recipe(ingredients)

    else:

        messages.error(request, "Please enter some ingredients.")

    return render(
    request,
    "recipes/ai_recipe.html",
    {
        "recipe": recipe,
        "ingredients": ingredients
    }
)
@api_view(["GET"])
def api_recipes(request):

    recipes = Recipe.objects.all()

    serializer = RecipeSerializer(recipes, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def api_categories(request):

    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def api_recipe_detail(request, slug):

    recipe = get_object_or_404(Recipe, slug=slug)

    serializer = RecipeSerializer(recipe)

    return Response(serializer.data)