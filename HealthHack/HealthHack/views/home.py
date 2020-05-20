from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
	return render(request, 'pages/home.html')

def redirectHome(request):
	return redirect("/")
