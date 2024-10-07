
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .forms import CustomUserCreationForm
from .views import SignupView
from django.urls import resolve

class CustomUserTest(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username="lerton",
            email="josinelerton@gmail.com",
            password="josineoffsec"
        )
        self.assertEqual(user.username, "lerton")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="margarida",
            email="margarida@gmail.com"
            )
        
        self.assertEqual(superuser.username, 'margarida')
        self.assertEqual(superuser.email, 'margarida@gmail.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)


class SignupTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_url(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_signup_template(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_signup_view(self):
        view = resolve(reverse('signup'))
        self.assertEqual(view.func.__name__, SignupView.as_view().__name__)
