from django.test.testcases import SimpleTestCase
from django.urls import resolve, reverse
from pages.views import HomePageView


class PagesTest(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_home_page_url_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
    
    def test_home_page_url_uses_right_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)