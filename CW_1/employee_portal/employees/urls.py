from django.urls import path
from employees.views import weather


urlpatterns = [
    path('weather/' , weather)
]