from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Low fidelity prototype.html')

def course(request):
    return render(request, 'Course.html')

def home(request):
    return render(request, 'Low fidelity prototype.html')

def daily_task(request):
    return render(request, 'Daily task.html')

def profile(request):
    return render(request, 'Profile.html')

def world_rankings(request):
    return render(request, 'World_rankings.html')

