from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    if width >= 1 and height >= 1:
        return HttpResponse(f'Площадь прямоугльника размером {width}х{height} равна {width * height}')
    else:
        return HttpResponseNotFound(f'Ты ваще в курсе что стороны должны быть больше единицы?')


def get_square_area(request, side: int):
    if side >= 1:
        return HttpResponse(f'Площадь квадрата со сторонами {side}х{side} равна {side * side}')
    else:
        return HttpResponseNotFound(f'Ты ваще в курсе что стороны должны быть больше единицы?')


def get_circle_area(request, radius: int):
    if radius >= 1:
        return HttpResponse(f'Площадь круга с радиусом {radius} равна {3.14 * radius ** 2}')
    else:
        return HttpResponseNotFound(f'Ты ваще в курсе что радиус должен быть больше единицы?')












