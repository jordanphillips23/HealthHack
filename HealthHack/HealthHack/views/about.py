from django.shortcuts import render
from django.http import HttpResponse
from ..loadData import loadData

def about(request):
	return render(request, 'pages/std/about.html', context = loadData())
