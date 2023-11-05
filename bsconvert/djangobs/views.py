from django.shortcuts import render, redirect
from .models import contact_detail
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')


 # You'll need to create the ContactForm

def home_msg(request):
    if request.method == 'POST':
          reg_dis = contact_detail(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'], message=request.POST['message'])
          reg_dis.save()
          return render (request,'index.html',{'reg_dis'=reg_dis,'msg'="message sent!!!"})
          return redirect('index')  # Redirect back to the index page
    

    return redirect('index.html')  # If the form submission fails, redirect back to the index page


