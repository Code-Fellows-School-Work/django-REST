from django.db import models
from django.contrib.auth import get_user_model

class Companie(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


    def __str__(self):
        return self.name