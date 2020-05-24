from django.shortcuts import render
from django.http import HttpResponse
from ..loadData import loadData

def submittedContact(request):
	return render(request, 'pages/submittedContact.html', context = loadData())
