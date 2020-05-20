from django.contrib import admin
from .models import company, dailyAverage, log

# Registering Models to the admin page here
admin.site.register(company)
admin.site.register(dailyAverage)
admin.site.register(log)
