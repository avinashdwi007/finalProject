from django.db import models

# Create your models here.

class data(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)

    def __str__(self):
        return self.username