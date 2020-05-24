"""HealthHack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HealthHack.views import home, about, contact, company, searchList
from HealthHack.api import change
urlpatterns = [
    # admin path, autogenerated
    path('admin/', admin.site.urls, name = "admin"),
    # Home pages / and  /home
    path('', home.home, name = "home"),
    path('home/', home.redirectHome, name = "redirect home"),
    path('Home/', home.redirectHome, name = "redirect home"),

    # About page
    path('about/', about.about, name = "about"),
    path('About/', about.about, name = "about"),

    # Contact page
    path('contact/', contact.contact, name = "contact"),
    path('Contact/', contact.contact, name = "contact"),

    path('company', company.company, name = "company"),

    path('searchList', searchList.searchList, name = "search list"),

    # api endpoints
    path('api/change', change.change, name = "change")
]
