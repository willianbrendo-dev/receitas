from recipes.models import Recipes, Category
from django.contrib.auth.models import User
from django.test import TestCase

class RecipeModelsTest(TestCase):
    
    def make_category(self, name='test'):
        return Category.objects.create(name=name)
    
    def make_author(self, username='testuser', password='testpass'):
        return User.objects.create_user(username=username, password=password)
    
    def make_recipe(
            self,
            category_data=None,
            author_data=None,
            title='test recipe',
            description='test description',
            slug='test-recipe',
            preparation_time=40,
            preparation_time_unit='Minutos',
            servings=8,
            servings_unit='Pessoas',
            preparation_steps='test steps',
            preparation_steps_is_html=False,
            is_published=True,
        ):
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}

        return Recipes.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )