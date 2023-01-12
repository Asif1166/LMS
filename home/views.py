
from django.shortcuts import render, redirect, HttpResponse

from .models import Course, Caurosel, Caurosel2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .forms import RegistrationForm, LoginForm
from django.views import View


# Create your views here.




def about(request):
    diction = {'title':'about'}
    return render(request, 'home/about.html', context=diction)

def course(request):
    diction = {'title':'course'}
    return render(request, 'home/course.html', context=diction)

def contact(request):
    diction = {'title':'contact'}
    return render(request, 'home/contact.html', context=diction)

def teacher(request):
    diction = {'title':'teacher'}
    return render(request, 'home/teacher.html', context=diction)

def exam(request):
    diction = {'title':'exam'}
    return render(request, 'home/exam.html', context=diction)

def library(request):
    diction = {'title':'library'}
    return render(request, 'home/library.html', context=diction)






class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'home/login.html', context={'form':form})
    
    def post(self, request):
        form = LoginForm(request=request, data=request.POST)
        if(form.is_valid()):
    
            return redirect('home')
        return render(request, 'home/login.html', context={'form':form})











def signup2(request):
    if(request.method == 'GET'):
        form = RegistrationForm()
        return render(request, 'home/signup.html', context={'form':form})
    
    form = RegistrationForm(request.POST)
    if(form.is_valid()):
        user = form.save()
        if(user is not None):
            return redirect('login')
        
    return render(request, 'home/signup.html', context={'form':form})

def signout(request):
    logout(request)
    return redirect('home')



def b_culture(request):
    diction = {'title':'culture'}
    return render(request, 'home/bangla_culture.html', context=diction)

def f_culture(request):
    diction = {'title':'culture'}
    return render(request, 'home/french_culture.html', context=diction)

def gallery(request):
    diction = {'title':'gallery'}
    return render(request, 'home/gallery.html', context=diction)


def board(request):
    diction = {'title':'tech-board'}
    return render(request, 'home/board.html', context=diction)

def LiveClass(request):
    diction = {'title':'live'}
    return render(request, 'home/live_class.html', context=diction)
