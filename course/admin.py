from django.contrib import admin
from .models import Sell_Course,Tag,Prere,Learning,Video,UserCourse,Payment
# Register your models here.

    
    
class VideoAdmin(admin.TabularInline):
    model = Video
    
class TagAdmin(admin.TabularInline):
    model = Tag
    
class PrereAdmin(admin.TabularInline):
    model = Prere
    
class LearningAdmin(admin.TabularInline):
    model = Learning
    
class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrereAdmin, VideoAdmin]
    

admin.site.register(Sell_Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(UserCourse)
admin.site.register(Payment)
