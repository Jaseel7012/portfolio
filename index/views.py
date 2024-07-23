from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from admin_app.models import Profile
# Create your views here.
def index(request):
    profile=Profile.objects.get(username=request.user.username)

    return render(request,'user/index.html',{'profile':profile})

def about(request):
    profile=Profile.objects.get(username=request.user.username)
    skills = [skill for skill in profile.skills.all()]
    return render(request,'user/about.html',{'profile':profile,'skills':skills})

def contact(request):
    profile=Profile.objects.get(username=request.user.username)
    
    return render(request,'user/contact.html',{'profile':profile})
def skills(request):
    profile=Profile.objects.get(username=request.user.username)
    skills = [skill for skill in profile.skills.all()]
    print(skills)
    return render(request,'user/skills.html',{'profile':profile,'skills':skills})
def userRegister(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email =request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword :
            if User.objects.filter(username=username).exists():
                return redirect('register')
            else :
                user = User.objects.create_user(username=username,
                                                email=email,password=password)
                user.save()
                return redirect('login')
        else :
            return redirect('register')

    return render(request,'account/register.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            if username == 'admin' and password=='1234':
                auth.login(request,user)
                return redirect('list')
            else:
                auth.login(request,user)
                profile=Profile.objects.filter(username = request.user.username).exists()
                print(profile)
                if profile:
                    return redirect('index')
                else :
                    messages.info(request,'Your profile Not updated.. ;')
                    return redirect('/')
        else :
            messages.info(request,'Invalid Credential')
            return redirect('login')
    return render(request,'account/login.html')

def logoutUser(request):
    auth.logout(request)
    return redirect('login')