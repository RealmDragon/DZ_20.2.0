from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contact(request):
    return render(request, 'catalog/contact.html')

def index(request):
    return render(request, 'catalog/index.html')