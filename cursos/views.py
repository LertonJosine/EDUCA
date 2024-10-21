from django.views.generic import ListView, DetailView, CreateView
from .models import Curso
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

class ListCoursesView(ListView):
    model = Curso
    context_object_name = 'courses'
    template_name = 'all_courses.html'


class CourseDetailsPageView(DetailView):
    model = Curso
    template_name = 'course_details.html'
    context_object_name = 'course'


class CreateCourseView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Curso
    fields = ['trainer', 'name', 'price', 'sits', 'cover', 'resume']
    template_name = 'create_course.html'
    permission_required = ('is_superuser')
    



