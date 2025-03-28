from django.urls import resolve
from recipes import views
from .test_recipe_model_test import RecipeModelsTest


class RecipeViewsTest(RecipeModelsTest):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html') 

    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_returns_404_if_no_recipes_found(self):
        response = self.client.get('/')
        self.assertIn('No recipe found here', response.content.decode('utf-8'))

    def test_recipe_category_view_function_is_correct(self):
        view = resolve('/recipe/category/1/')
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get('/recipe/category/1000/')
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve('/recipe/1/')
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get('/recipe/1000/')
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_templates_loads_recipes(self):
        self.make_recipe()
        response = self.client.get('/')
        content = response.content.decode('utf-8')
        # response_context = response.context
        self.assertIn('test recipe', content)