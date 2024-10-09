from django.views.generic import ListView, DetailView
from .models import Curso

class ListCoursesView(ListView):
    model = Curso
    context_object_name = 'courses'
    template_name = 'all_courses.html'


class CourseDetailsPageView(DetailView):
    model = Curso
    template_name = 'course_details.html'
    context_object_name = 'course'
