from django.db import models


# Create your models

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    
    def __str__(self):
        return str(self.pk)+" "+self.name