from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ..loadData import loadData

def home(request):
	return render(request, 'pages/std/home.html', context = loadData())

def redirectHome(request):
	return redirect("/")
