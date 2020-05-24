from django.shortcuts import render
from django.http import HttpResponse
from ..loadData import loadData
from django.shortcuts import redirect

def contact(request):
	if request.method == "GET":
		if "name" in request.GET:
			return redirect("/submitted")
	return render(request, 'pages/std/contact.html', context = loadData())
