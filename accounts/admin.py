from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomAdmin(admin.ModelAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomAdmin)

