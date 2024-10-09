from django.test import TestCase
from django.urls import resolve, reverse
from .models import Curso
from django.contrib.auth import get_user_model
from .views import ListCoursesView

class CursosTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@gmail.com'
        )
        self.course = Curso.objects.create(
            trainer=self.user,
            name='test course',
            resume='test course creation',
            cover='./media/course-1.jpg',
            price=20.00,
            sits=10         
            
        )
    
        url = reverse('all_courses')
        self.response = self.client.get(url)
    
    def test_list_courses_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_course_creation(self):
        self.assertEqual(self.course.trainer, self.user)
        self.assertEqual(self.course.name, 'test course')
        self.assertEqual(self.course.resume, 'test course creation')
        self.assertEqual(self.course.price, 20.00)
        self.assertEqual(self.course.sits, 10)
    
    def test_list_courses_template(self):
        self.assertTemplateUsed(self.response, 'all_courses.html')
        self.assertContains(self.response, 'Courses')
    
    def test_list_courses_view_used(self):
        view = resolve(reverse('all_courses'))
        self.assertEqual(view.func.__name__, ListCoursesView.as_view().__name__)
    