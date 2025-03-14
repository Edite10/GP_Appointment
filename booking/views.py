from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Doctor, Appointment
from .forms import AppointmentForm

def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'booking/home.html', {'doctors': doctors})

def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'booking/book_appointment.html', {'form': form})

