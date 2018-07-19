from django.shortcuts import render
import json
import requests
# Create your views here.


def index(request):
    css_files = ['css/testing.css','css/landing.css']

    #get ip 
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

        print(ip)

    #Getting current weather from api
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Seattle&units=imperial&APPID=ca5717e90c7e247434710b5bda9b332b')
    geodata = json.loads(response.content.decode('utf-8'))
    temperature = int(geodata['main']['temp'])


    my_dict = {'title': 'Code Solutions', 'css': css_files,'temp':temperature}

    return render(request,'landing/index.html', context = my_dict)


