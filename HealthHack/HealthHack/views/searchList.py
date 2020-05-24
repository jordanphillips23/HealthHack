from django.shortcuts import render
from django.http import HttpResponse
from ..loadData import loadData
from ..models import company

def searchList(request):
    context = loadData()
    print(request.GET)
    if request.method == "GET":
        if "type" in request.GET and "zip" in request.GET:
            print(request.GET["type"])
            context["results"] = company.objects.filter(type = request.GET["type"], zip = request.GET["zip"]).values()
            print(context["results"])
            return render(request, 'pages/searchList.html', context = context)
    return HttpResponse(status=400)
