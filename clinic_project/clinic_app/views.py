from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Messages, Depatrments, Doctorlist
from .forms import AppointmentForm
# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    dep = Depatrments.objects.all()
    doctorslist = Doctorlist.objects.all()
    
    if request.method=='POST':
        fm= AppointmentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/index')
    else:
        fm= AppointmentForm()
    return render (request, 'index.html', {'dp':dep, 'doclis':doctorslist, 'form':fm})

def about(request):
    
    doctorslist = Doctorlist.objects.all()
    return render (request, 'about.html', {'doclis':doctorslist})

def appointment(request):
    if request.method=='POST':
        fm= AppointmentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/index')
    else:
        fm= AppointmentForm()
    return render (request, 'appointment.html', {'form':fm})

def contact(request):
    
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        subject= request.POST['subject']
        message= request.POST['message']
        
        newmsg = Messages.objects.create(name=name, email=email, subject=subject, message=message)
        newmsg.save()
        return redirect('/index')
    
    
    return render (request, 'contact.html')

def feature(request):
    return render (request, 'feature.html')

def service(request):
    
    dep = Depatrments.objects.all()
    return render (request, 'service.html', {'dp': dep})

def team(request):
    
    doctorslist = Doctorlist.objects.all()
    return render (request, 'team.html', {'doclis': doctorslist})

