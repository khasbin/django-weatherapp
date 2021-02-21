from django.shortcuts import render, HttpResponse
import requests
from .models import City
# Create your views here.

def home(request):
    url = "http://api.weatherapi.com/v1/current.json?key=ac457ea4fc2a4b4fa1b51740210602&q={}"

    city = request.GET.get("cname")

    r = requests.get(url.format(city)).json()
    weather = {
        'city':city,
        'temperature':r['current']['temp_c'],
        'condition':r['current']['condition']['text'],
        'icon':r['current']['condition']['icon']
    }
    context = {'weather':weather}

    return render(request,'weatherapp/index.html',context)
    

def add(request, name):
    name_count = City.objects.filter(name = name).count()
    err_msg= ''
    if name_count == 0:
        ins = City(name = name)
        ins.save()
    else:
        err_msg ="The city is already present in the database"
    
    cities = City.objects.all()

    weather_list = []

    url = "http://api.weatherapi.com/v1/current.json?key=ac457ea4fc2a4b4fa1b51740210602&q={}"

    for city in cities:
        r = requests.get(url.format(city)).json()
        weather = {
        'city':city,
        'temperature':r['current']['temp_c'],
        'condition':r['current']['condition']['text']
        }
        weather_list.append(weather)

    context = {"weather_list": weather_list, "err_msg": err_msg}
    return render(request,'weatherapp/index.html',context)

