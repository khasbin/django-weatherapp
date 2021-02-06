from django.shortcuts import render, HttpResponse
import requests
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
    