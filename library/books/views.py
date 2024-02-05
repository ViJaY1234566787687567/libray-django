from django.shortcuts import render
from books.models import Book
from books.forms import bookform


def home(request):
    return  render(request,'home.html')

def view(request):
    k=Book.objects.all()#to select details from Book table
    return  render(request,'viewbooks.html',{'b':k})
def add(request):
    if(request.method=='POST'):#After submittion
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        b=Book.objects.create(title=t,author=a,price=p)
        b.save()
        return view(request)
    return  render(request,'addbooks.html')

def add1(request):
    form=bookform()
    return render(request,'addbooks1.html',{'form':form})
