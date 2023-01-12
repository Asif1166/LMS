from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=30)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='img', default='')
    teacher_name = models.CharField(max_length=30)
    total_hours = models.IntegerField()
    total_students = models.IntegerField()

    def __str__(self):
        return self.course_name

class Caurosel(models.Model):
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='img', default='')
    def __str__(self):
        return self.title
    
class Caurosel2(models.Model):
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='img', default='')
    def __str__(self):
        return self.title

    class Caurosel3(models.Model):
        title = models.CharField(max_length=50)
        heading = models.CharField(max_length=100)
        description = models.CharField(max_length=100)
        picture = models.ImageField(upload_to='img', default='')
        def __str__(self):
            return self.title
    