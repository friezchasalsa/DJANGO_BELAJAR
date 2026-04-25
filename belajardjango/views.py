from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def biodata(request):
    return render(request, 'biodata.html')

def blog(request):
    return render(request, 'blog.html')

def kontak(request):
    return render(request, 'kontak.html')