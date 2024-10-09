from django.urls import path
from .views import ListCoursesView, CourseDetailsPageView

urlpatterns = [
    path('all/', ListCoursesView.as_view(), name="all_courses"),
    path('course_details/<int:pk>/', CourseDetailsPageView.as_view(), name='course_details'),
]
