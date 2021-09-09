from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User,Apointment
from datetime import date

estados = ('Done','Pending','initial','Missed')
# Create your views here.
def index(request):
    usuario =User.objects.get(id=request.session['user_id'])
    citas = usuario.appointment.all()
    
    return render(request, 'index.html',
    {'citas':citas,'citaspasadas':pastappointment(citas)})

def add(request):
    
    if request.method == 'POST':
        print(request.POST['st'])
        Apointment.objects.create(
            task=request.POST['task'],
            date=request.POST['date'],
            status=request.POST['st'],
            user=User.objects.get(id=request.session['user_id'])
        )
        return redirect('index')

    
    return render(request, 'add.html',{'estados':estados})

def pastappointment(citas):
    citaspasadas  = []
    for cita in citas:
        if cita.date < date.today():
            citaspasadas.append(cita)
    return citaspasadas