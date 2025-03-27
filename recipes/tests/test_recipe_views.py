from django.test import TestCase
from django.urls import resolve
from recipes import views
from django.contrib.auth.models import User
from recipes.models import Recipes, Category





class RecipeViewsTest(TestCase):

    
    def setUp(self):
        # Set up non-modified objects used by all test methods
        user =User.objects.create(username='sophia', first_name='Big', last_name='Bob', email='sophia@email.com', )

        category1 = Category.objects.create(
            name='morango',
        )

        category2 = Category.objects.create(
            name='banana',
        )

        recipe1 = Recipes(
            title="Bolo de Chocolate",
            description="Bolo de chocolate úmido e delicioso.",
            slug="bolo-de-chocolate",
            preparation_time=45,
            preparation_time_unit="minutos",
            servings=8,
            servings_unit="fatias",
            preparation_steps="Misture os ingredientes secos, adicione os líquidos e asse no forno.",
            preparation_steps_is_html=False,
            cover="bolo_de_chocolate.jpg",
            author=user,  # Supondo que o usuário com id=1 existe
            category=category1  # Supondo que a categoria com id=1 existe
        )
        recipe1.save()

        recipe2 = Recipes(
            title="Salada de Frutas",
            description="Salada colorida e refrescante.",
            slug="salada-de-frutas",
            preparation_time=15,
            preparation_time_unit="minutos",
            servings=4,
            servings_unit="porções",
            preparation_steps="Corte as frutas e misture em uma tigela.",
            preparation_steps_is_html=False,
            cover="salada_de_frutas.jpg",
            author=user,  # Supondo que o usuário com id=2 existe
            category=category1  # Supondo que a categoria com id=2 existe
        )
        recipe2.save()

        recipe3 = Recipes(
            title="Feijoada",
            description="Prato típico brasileiro, feito com feijão preto e carnes.",
            slug="feijoada",
            preparation_time=120,
            preparation_time_unit="minutos",
            servings=6,
            servings_unit="porções",
            preparation_steps="Cozinhe o feijão e as carnes, tempere e sirva com arroz e farofa.",
            preparation_steps_is_html=False,
            cover="feijoada.jpg",
            author=user,  # Supondo que o usuário com id=3 existe
            category=category1  # Supondo que a categoria com id=3 existe
        )
        recipe3.save()
        print(Recipes.objects.all())
        print(Category.objects.all().values_list('id' ,'name'))


    def test_create_book(self):
        self.assertEquals(Category.objects.all().count(), 2)

        

    def test_recipe_home_view_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve('/recipe/category/1/')
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve('/recipe/1/')
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_returns_status_code_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_view_returns_status_code_200(self):
        response = self.client.get('/recipe/category/2/')
        self.assertEqual(response.status_code, 200)

    
    def test_recipe_detail_view_returns_status_code_200(self):
        response = self.client.get('/recipe/1/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')      

    def test_recipe_category_view_uses_correct_template(self):
        response = self.client.get('/recipe/category/1/')
        self.assertTemplateUsed(response, 'category.html')

    def test_recipe_detail_view_uses_correct_template(self):
        response = self.client.get('/recipe/1/')
        self.assertTemplateUsed(response, 'recipes/templates/recipe.html')

    