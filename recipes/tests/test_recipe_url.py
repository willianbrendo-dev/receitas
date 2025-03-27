from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('categories-recipe', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipe/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes-recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipe/1/')