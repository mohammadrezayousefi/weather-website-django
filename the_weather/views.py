from django.shortcuts import render, redirect
from .forms import CityForm
from django.contrib import messages
import requests
from .models import City


def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a7e1f8b46c813fd91514a3f3d624b0ef'
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('name')
            count = City.objects.all().filter(name=city).count()
            r = requests.get(url.format(city)).json()
            if r['cod'] == 200:
                if count == 0:
                    form.save()
            else:
                messages.warning(request, f'شهر {city} وجود ندارد ، شاید نام شهر را اشتباه وارد کرده اید.')
                form = CityForm()
                return redirect('home')
    else:
        form = CityForm()
        city = 'Tehran'
        r = requests.get(url.format(city)).json()

    city_weather = {
        'form': form,
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    return render(request, 'weather/weather.html', city_weather)
