from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Curso(models.Model):
    trainer = models.ForeignKey(get_user_model(), models.CASCADE)
    name = models.CharField(max_length=200)
    resume = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sits = models.IntegerField()
    cover = models.ImageField(upload_to='media/')

    
    def get_absolute_url(self):
        return reverse("home")
    
    def __str__(self) -> str:
        return self.name[:100]

    