from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Sell_Course(models.Model):
    name = models.CharField(max_length=30, null=False)
  
    slug = models.CharField(max_length=50, null=False, unique=True)
    description = models.CharField(max_length=300, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='media/thumbnail')
    date = models.DateTimeField(auto_now_add= True)
    resource = models.FileField(upload_to='media/resource')
    length = models.IntegerField(null=False)
    
    
    def __str__(self):
        return self.name
    
class CourseProperty(models.Model):
    description = models.CharField(max_length=200, null=False)
    course = models.ForeignKey(Sell_Course, null=False, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass
    
class Prere(CourseProperty):
    pass
    
class Learning(CourseProperty):
    pass

class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Sell_Course, null=False, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    course_video = models.FileField(upload_to="img", default='')
    video_id = models.CharField(max_length=200, null=False)
    is_preview = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
class UserCourse(models.Model):
    
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Sell_Course, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add= True)
  
    def __str__(self):
        return f'{self.user.username} - {self.course.name}'
    
class Payment(models.Model):
    order_id = models.CharField(max_length = 50 , null = False)
    payment_id = models.CharField(max_length = 50)
    user_course = models.ForeignKey(UserCourse , null = True , blank = True ,  on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    course = models.ForeignKey(Sell_Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
