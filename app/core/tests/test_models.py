from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from core import models

def create_user(email='user@example.com', password='testpass123'):
    """Create a return a new user."""
    return get_user_model().objects.create_user(email, password)
class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = '<testpass123'
        user = get_user_model().objects.create_user(
            email=email
            , password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','123')

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@123example.com',
            'test123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self): #Test recioe model
        """Test creating a new recipe"""
        user = get_user_model().objects.create_user(
            'test@1223example',
            'testpass123'
        )
        recipe = models.Recipe.objects.create(
            user = user,
            title='Sample recipes name',
            time_minutes=5,
            price=Decimal('5.3'),
            description='Sample recipe description',
        )
        self.assertEqual(str(recipe), recipe.title)
    def test_create_tag(self):  # Test Tag Model
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag1')
        self.assertEqual(str(tag), tag.name)

    def test_create_ingredient(self):

        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='Ingredient1'
        )
        self.assertEqual(str(ingredient), ingredient.name)

