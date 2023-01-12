from django.shortcuts import render, HttpResponse, redirect
from .models import Sell_Course, Video
from home.models import Caurosel, Caurosel2
from django.views.generic import ListView




# Create your views here.
def home(request):
    
    courses = Sell_Course.objects.all()
    caurosels = Caurosel.objects.all()
    caurosels2 = Caurosel2.objects.all()
    return render(request, 'home/home.html', context={'title':'Home',"courses" : courses, 'caurosels':caurosels, 'caurosels2':caurosels2})

def CoursePage(request, slug):
    
    course = Sell_Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1
    video = Video.objects.get(serial_number = serial_number, course = course)
    print (video)
    
    if((request.user.is_authenticated is False) and (video.is_preview is True)):
        return redirect('login')
    context = {
        'course': course ,
        'serial_number' : serial_number, 
        'video' : video,
        'videos':videos
        }
    
    return render(request, 'home/coursepage.html', context)

def Enroll(request, slug):
    courses = Sell_Course.objects.all()
    course = Sell_Course.objects.get(slug = slug)
    
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'home/enroll.html', context={'course':course, 'courses':courses})