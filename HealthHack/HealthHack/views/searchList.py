from django.shortcuts import render
from django.http import HttpResponse
from ..loadData import loadData
from ..models import company

def searchList(request):
    context = loadData()
    print(request.GET)
    if request.method == "GET":
        if "type" in request.GET and "zip" in request.GET:
            currentQuery = company.objects
            if request.GET["type"] == "Type" and request.GET["zip"] == "":
                currentQuery = currentQuery.all()
            elif request.GET["type"] == "Type" :
                currentQuery = currentQuery.filter(zip = request.GET["zip"])
            elif request.GET["zip"] == "":
                currentQuery = currentQuery.filter(type = request.GET["type"])
            else:
                currentQuery = currentQuery.filter(zip = request.GET["zip"], type = request.GET["type"])
            context["results"] = currentQuery.values()

            return render(request, 'pages/searchList.html', context = context)
    return HttpResponse(status=400)
