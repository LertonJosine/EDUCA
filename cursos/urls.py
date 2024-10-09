from django.urls import path
from .views import ListCoursesView

urlpatterns = [
    path('all/', ListCoursesView.as_view(), name="all_courses")
]
