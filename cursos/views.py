from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso

class ListCoursesView(ListView):
    model = Curso
    context_object_name = 'courses'
    template_name = 'all_courses.html'
