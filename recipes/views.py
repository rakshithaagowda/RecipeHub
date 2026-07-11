from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
from django.db.models import Q
from django.core.paginator import Paginator


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

    context = {
        "recipe": recipe,
    }

    return render(request, "recipes/recipe_detail.html", context)
def recipe_list(request):
    recipe_list = Recipe.objects.all()

    # Get all categories for dropdown
    categories = Category.objects.all()

    # Get selected category
    category_slug = request.GET.get("category")

    if category_slug:
        recipe_list = recipe_list.filter(category__slug=category_slug)

    # Pagination
    paginator = Paginator(recipe_list, 6)

    page_number = request.GET.get("page")
    recipes = paginator.get_page(page_number)

    context = {
        "recipes": recipes,
        "categories": categories,
        "selected_category": category_slug,
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