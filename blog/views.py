from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


def index(request):
    return render(request, 'blog/title.html')


def kianu(request):
    data = {'year_born': 1992,
            'city_born': 'Kazan',
            'movie_name': 'BIG',
            }
    return render(request, 'blog/kianu.html', data)
