from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm


class SignupView(CreateView):
    model = get_user_model()
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    


    