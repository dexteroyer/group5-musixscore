from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    genre = models.CharField(max_length=200)



class