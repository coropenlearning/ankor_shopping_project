from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'order/index.html')

def payment(request):
    return redirect('http://localhost:7000')
