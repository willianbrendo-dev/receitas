from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.factory import make_recipe
from .models import Recipes


# Create your views here.

def home(request):
    recipes = Recipes.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'home.html', context={
        'recipes': recipes
    })

def category(request, category_id):
    recipes = get_list_or_404(
        Recipes.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id'))
        


    return render(request, 'category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipes, pk=id, is_published=True)
    
    return render(request, 'recipe.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })