from django.shortcuts import render

# Create your views here.
def java(r):
    return render(r,'java/home.html')
def script(r):
    return render(r,'java/script.html')