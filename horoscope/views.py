from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    zodiacs = list(zodiac_dict)
    # f'<li> <a href="{redirect_url}"> {sign.title()} </a> </li>'
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


def types(request):
    elements = list(zodiac_element)
    rez = ''
    for sign in elements:
        redirect_url = reverse('horoscope_elements', args=[sign])
        rez += f'<li><a href="{redirect_url}">{sign.title()}</a></li>'
    response = f'<h1><ol>{rez}</ol></h1>'
    return HttpResponse(response)


def element(request, elements):
    rez = ''
    for sign in zodiac_element[elements]:
        redirect_url = reverse('horoscope-name', args=[sign])
        rez += f'<li><a href="{redirect_url}">{sign.title()}</a></li>'
    response = f'<h1><ol>{rez}</ol></h1>'
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {'name': description,
            'wrong': sign_zodiac}
    return render(request, 'horoscope/info_zodiac.html', data)


def get_info_about_sign_zodiac_number(request, sign_zodiac: int):
    sign_zodiac_dict = list(zodiac_dict)
    if int(sign_zodiac) > len(sign_zodiac_dict):
        return HttpResponseNotFound(f'Елки палки, ВСЕГО 12 ЗНАКОВ, а не {sign_zodiac}')
    name_zodiac = sign_zodiac_dict[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)
