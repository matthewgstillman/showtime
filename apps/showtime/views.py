from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    return render(request, 'showtime/index.html')

def send_request(request):
    try:
        response = requests.get(
            url="https://api.cinepass.de/v4/movies/",
            params={
                "countries": "US",
            },
            headers={
                "X-API-Key": yE5PUTGkOkyJoimmgibwO4Q5ROmmbLXp,
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

def alltheaters(request):
    url = ('https://api.cinepass.de/v4/cinemas/?apikey=yE5PUTGkOkyJoimmgibwO4Q5ROmmbLXp')
    response = requests.get(url)
    showtimes = response.json()
    print(response)
    print showtimes
    context = {
        'response': response,
        'showtimes': showtimes,
    }
    return render(request, 'showtime/alltheaters.html', context)


def cities(request):
    url = ('https://api.cinepass.de/v4/cities/?apikey=yE5PUTGkOkyJoimmgibwO4Q5ROmmbLXp')
    response = requests.get(url)
    cities = response.json()
    print(response)
    print(cities)
    context = {
        'response': response,
        'cities': cities,
    }
    return render(request, 'showtime/cities.html', context)


def movies(request):
    url = ('https://api.cinepass.de/v4/movies/?apikey=yE5PUTGkOkyJoimmgibwO4Q5ROmmbLXp')
    response = requests.get(url)
    movies = response.json()
    print(response)
    print(movies)
    context = {
        'response': response,
        'movies': movies,
    }
    return render(request, 'showtime/movies.html', context)