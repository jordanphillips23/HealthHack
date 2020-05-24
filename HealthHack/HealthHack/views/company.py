from django.shortcuts import render
from django.http import HttpResponse
from ..loadData import loadData
from ..models import company as companyDB
from ..models import dailyAverage
import datetime




# shows the company specific page
# expecting get request with the company
def company(request):
    if request.method == "GET":
        context = loadData()
        # checks to see if an id has been passed in
        if "company" in request.GET:
            # get the current company and store it in the context
            context["company"] = companyDB.objects.get(id = int(request.GET["company"]))

            # get the data in the correct order
            filteredData = dailyAverage.objects.filter(companyID = context["company"])
            hourMapper = []
            for i in range(1,24):
                hourMapper.append(datetime.time(i, 0 , 0))
            hourMapper.append(datetime.time(0, 0, 0))
            out = []

            for time in hourMapper:
                out.append(filteredData.get(time = time).population)

            # pass in the hourly data to be used for the chart
            context["averages"] = out



            return render(request, 'pages/company.html', context = context)
    return HttpResponse(status=400)
