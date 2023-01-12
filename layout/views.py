from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import contact

# Create your views here.
def layout(request):
    
    
    
    return render(request, 'layout/layout.html' )

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        en=contact(name=name,email=email,subject=subject,message=message)
        
        en.save()
        messages.success(request, "message sent successfully")
    return redirect('signin')

def signup(request):
    diction = {'title':'signup'}
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        messages.success(request, "account created successfully")
        return redirect('signin')

    return render(request, 'authentication/signup.html', context=diction)

def signin(request):
    diction = {'title':'sign in'}
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        
        user = authenticate(username = username, password = pass1)
        
        if user is not None:
            login(request, user)
            
            return render(request, 'home/teacher.html')
            
        else:
            messages.error(request, "error login")
            return redirect('signup')
        
    return render(request, 'authentication/signin.html', context=diction)

def signout(request):
    diction = {'title':'signout'}
    return render(request, 'authentication/signout.html', context=diction)