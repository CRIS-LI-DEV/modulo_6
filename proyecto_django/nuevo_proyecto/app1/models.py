from django.db import models
from django.contrib.auth.models import User



class PerfilDeUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.first_name} | {self.user.last_name} | {self.profesion}"