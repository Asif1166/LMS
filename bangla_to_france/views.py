from django.shortcuts import render
from .models import Item, Video

# Create your views here.
def video(request):

    videos = Item.objects.all()
    diction = {'videos':videos}
    
    return render(request, 'vid/video2.html', context=diction)

def vida1(request):
    videos = Item.objects.all()
    diction = {'videos':videos}
    return render(request, 'vid/vida1.html', context=diction)

def vida2(request):
    videos2 = Video.objects.all()
    diction = {'videos2':videos2}
    
    return render(request, 'vid/vida2.html', context=diction)


    