from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SignupView(CreateView):
    model = get_user_model()
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    

class ProfilePageView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'registration/profile.html'
    
    def test_func(self):
        user = self.request.user
        return user == self.get_object()
    
