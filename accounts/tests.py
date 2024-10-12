
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .forms import CustomUserCreationForm
from .views import SignupView, ProfilePageView
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
        self.assertContains(self.response, 'Signup')
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_signup_view(self):
        view = resolve(reverse('signup'))
        self.assertEqual(view.func.__name__, SignupView.as_view().__name__)


class ProfileTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@gmail.com',
            password='test123'
        )
        
        self.user_2 = get_user_model().objects.create_user(
            username='test2',
            email='test2@gmail.com',
            password='test123'
        )
        
        self.client.login(username=self.user.username, password='test123')
        url = reverse('profile', args=[self.user.pk])
        self.response = self.client.get(url)
    
    def test_profile_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_profile_user_access_only_his_data(self):
        response = self.client.get(reverse('profile', args=[self.user_2.pk]))
        self.assertEqual(response.status_code, 403)
    
    def test_profile_template(self):
        self.assertTemplateUsed(self.response, 'registration/profile.html')
        self.assertContains(self.response, 'Profile')
    
    def test_profile_uses_correct_view(self):
        view = resolve(reverse('profile', args=[self.user.pk]))
        self.assertEqual(view.func.__name__, ProfilePageView.as_view().__name__)
        