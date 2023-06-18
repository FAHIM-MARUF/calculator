# calculator/views.py
from django.shortcuts import render

def calculator(request):

    return render(request, 'index.html')
