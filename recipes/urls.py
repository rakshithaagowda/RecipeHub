from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Recipe Detail Page
    path("recipe/<slug:slug>/", views.recipe_detail, name="recipe_detail"),
]