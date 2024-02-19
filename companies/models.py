from django.db import models

class Companies(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


    def __str__(self):
        return self.name