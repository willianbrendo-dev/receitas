from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/category/<int:category_id>/', views.category, name='categories-recipe'),
    path('recipe/<int:id>/', views.recipe, name='recipes-recipe'),
]