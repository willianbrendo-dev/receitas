from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)