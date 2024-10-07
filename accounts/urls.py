from django.urls import path
from .views import SignupView, ProfilePageView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='profile'),
]
