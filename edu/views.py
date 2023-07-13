from django.shortcuts import render
from . import views

# Create your views here.

def skill(request):
    context = {'skill' : 'active'}
    return render(request , 'edu/skill.html' , context)
