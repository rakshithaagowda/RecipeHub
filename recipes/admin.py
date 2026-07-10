from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image_preview")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px; object-fit:cover;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "difficulty",
        "servings",
        "prep_time",
        "cook_time",
        "featured",
        "created_at",
        "image_preview",
    )

    list_filter = (
        "category",
        "difficulty",
        "featured",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "ingredients",
    )

    list_editable = ("featured",)

    prepopulated_fields = {"slug": ("title",)}

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Recipe Information", {
            "fields": (
                "title",
                "slug",
                "category",
                "hero_image",
                "featured",
            )
        }),

        ("Recipe Details", {
            "fields": (
                "description",
                "ingredients",
                "instructions",
            )
        }),

        ("Cooking Details", {
            "fields": (
                "prep_time",
                "cook_time",
                "servings",
                "difficulty",
                "calories",
            )
        }),

        ("Dates", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def image_preview(self, obj):
        if obj.hero_image:
            return format_html(
                '<img src="{}" width="70" height="70" style="border-radius:10px; object-fit:cover;" />',
                obj.hero_image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"