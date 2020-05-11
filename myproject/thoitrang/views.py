from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def checkout(request):
    return render(request, 'checkout.html')
    
def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def details(request):
    return render(request, 'details.html')

def products(request):
    return render(request, 'products.html')

