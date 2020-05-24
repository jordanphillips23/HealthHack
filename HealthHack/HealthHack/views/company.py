from django.shortcuts import render
from django.http import HttpResponse
from ..loadData import loadData
from ..models import company as companyDB
from ..models import dailyAverage
import datetime





def company(request):
    if request.method == "GET":
        context = loadData()
        if "company" in request.GET:
            context["company"] = companyDB.objects.get(id = int(request.GET["company"]))
            filteredData = dailyAverage.objects.filter(companyID = context["company"])
            hourMapper = []
            for i in range(1,24):
                hourMapper.append(datetime.time(i, 0 , 0))
            hourMapper.append(datetime.time(0, 0, 0))
            out = []

            for time in hourMapper:
                out.append(filteredData.get(time = time).population)
            context["averages"] = out



            return render(request, 'pages/company.html', context = context)
    return HttpResponse(status=400)
