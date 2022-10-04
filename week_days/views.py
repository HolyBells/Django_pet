from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
todo_list_dict = {
    'monday': 'Необходимо разъебать в доте',
    'tuesday': 'Скорее всего в доте уже разъебано',
    'wednesday': 'Я хорош',
    'thursday': 'безумно хорош',
    'friday': 'в дотку надо',
    'saturday': 'ебать хорош',
    'sunday': 'снова в дотку',

}


def get_days_info(request, todo_list):
    description = todo_list_dict.get(todo_list, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Че, самый умный что-ли? Нет "{todo_list}" в списке дней недели')


def get_days_info_number(request, todo_list: int):
    return render(request, 'week_days/greeting.html')
