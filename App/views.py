from django.shortcuts import render

# Create your views here.
def home1(request):
    return render(request,'home.html')

def product(request):
    return render(request,'product.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')