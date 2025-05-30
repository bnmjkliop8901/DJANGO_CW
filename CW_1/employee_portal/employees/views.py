from django.shortcuts import render

# Create your views here.

from employees.models import RealTimeWeather


def weather(request):
    return render(request , 'weather1.html')