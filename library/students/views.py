from django.shortcuts import render
from students.models import Student
# Create your views here.
def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def view(request):
    k=Student.objects.all()#to select details from Book table
    return render(request,'viewstudents.html',{'s':k})