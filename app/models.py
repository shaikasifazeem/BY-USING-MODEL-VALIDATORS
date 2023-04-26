from django.db import models
from django.core import validators

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(5)])
    age=models.IntegerField()
    email=models.EmailField(validators=[validators.EmailValidator])
    re_enteremail=models.EmailField()
    

