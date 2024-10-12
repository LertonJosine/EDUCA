from django.forms import ModelForm
from .models import Curso


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['trainer', 'name', 'price', 'sits', 'resume']
        
        
