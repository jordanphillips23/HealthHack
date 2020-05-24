from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from ..models import company, log
import django

from django.views.decorators.csrf import csrf_exempt

# expected method is POST

@csrf_exempt
def change(request):
    if request.method == "POST":
        # checks if a company exists with the passed in api key
        if company.objects.filter(key = request.POST['key']).count() == 1:
            # updates the population for that company
            currentCompany = company.objects.get(key = request.POST['key'])
            currentCompany.currentPopulation = int(request.POST['population'])
            currentCompany.save()

            # creates a new log object to store the passed in data
            log.objects.create(companyId = currentCompany, population = request.POST['population'],
            date = request.POST['date'], time = request.POST['time'])

            # returns success code
            return HttpResponse(status = 200)
        else:
            # invalid data code
            return HttpResponse(status = 401)
    else:
        # invalid request type
	    return HttpResponse(status = 404)
