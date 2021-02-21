from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contact,doctors,patient,pharmacy,furniture,surgical_instruments,staff_supplies,room
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method=='POST':
        
        contact.name=request.POST["my_Name"]
        contact.email=request.POST["my_email"]
        contact.phoneno=request.POST["phoneno"]
        contact.message=request.POST["message"]
        Contact=contact.objects.create(name=contact.name,email=contact.email,phoneno=contact.phoneno,message=contact.message)
    return render(request,'index.html')
def Records(request):
    Fur=furniture.objects.all()
    
    Rooom=room.objects.all()
    return render(request,'H_record.html',{'Fur':Fur,'Rooom':Rooom})



def pharmacy_storage(request):
    Phar=pharmacy.objects.all()
    return render(request,'pharmacies.html',{'Phar':Phar})
def team(request):
    teams=doctors.objects.all()
    return render(request,'doctors.html',{'teams':teams})
def patientsdata(request):
    Patient=patient.objects.all()
    return render(request,'patients.html',{'Patient':Patient})

def register(request):
    if request.method=='POST':
        username=request.POST["register_username"]
        first_name=request.POST["register_First_name"]
        last_name=request.POST["register_Last_name"]
        email=request.POST["register_email"]
        password1=request.POST["register_password"]
        password2=request.POST["register_cpassword"]
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')

        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST["login_username"]
        password=request.POST["login_password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')