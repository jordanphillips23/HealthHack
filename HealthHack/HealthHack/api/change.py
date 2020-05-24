from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from ..models import company, log
import django

def change(request):
    if request.method == "POST":
        if company.objects.count(key = request['key']) == 1:
            currentCompany = company.objects.get(key = request['key'])
            currentCompany.currentPopulation = int(request['population'])
            currentCompany.save()
            log.objects.create(companyID = currentCompany, population = request['population'],
            date = request['date'], time = request['time'])
        else:
            return HttpResponse(status = 401)
    else:
	    return HttpResponse(status = 404)
