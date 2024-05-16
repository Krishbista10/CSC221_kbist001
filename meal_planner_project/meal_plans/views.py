from django.shortcuts import render

# Create your views here.
# meal_plans/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'meal_plans/home.html')
s