from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Rectangle with sides {width} x {height} has area {width * height}')


def get_rectangle_area_redirect(request, width: int, height: int):
    reverse_url = reverse('rectangle_url', args=[width, height])
    return HttpResponseRedirect(reverse_url)


def get_square_area(request, side: int):
    return HttpResponse(f'Square with sides {side} has area {side * side}')


def get_square_area_redirect(request, width: int):
    reverse_url = reverse('square_url', args=[width])
    return HttpResponseRedirect(reverse_url)


def get_circle_area(request, radius: int):
    return HttpResponse(f'Circle with radius {radius} has area {radius ** 2 * 3.14}')


def get_circle_area_redirect(request, radius: int):
    reverse_url = reverse('circle_url', args=[radius])
    return HttpResponseRedirect(reverse_url)
