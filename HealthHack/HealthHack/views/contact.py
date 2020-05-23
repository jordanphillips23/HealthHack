from django.shortcuts import render
from django.http import HttpResponse
from ..loadData import loadData

def contact(request):
	return render(request, 'pages/std/contact.html', context = loadData())
