from django.shortcuts import render
from .models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    context = {'home' : 'active'}
    return render(request , 'core/home.html' , context)
def contact(request):
    context = {'contact' : 'active'}
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        # phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        massage = request.POST.get("massage")
        contact = Contact(name=name , email=email ,  subject= subject , massage = massage , date = datetime.today())
        contact.save()
        # messages.success(request, 'your msg has been send...')
        print(massage)
    return render(request , 'core/contact.html' , context)
