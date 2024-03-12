from django.shortcuts import render,redirect
from django.contrib import messages
from .models import CallReq

# Create your views here.
def adminive(request):
    pass

def home(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        
        submit=CallReq.objects.create(name=name,email=email,phone=phone,description=desc).save()
        messages.success(request,"Send request succesful..")
        return redirect('/')
    return render(request,"home.html")