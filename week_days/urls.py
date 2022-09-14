from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('<int:todo_list>', views_week_days.get_days_info_number),
    path('<str:todo_list>', views_week_days.get_days_info, name='days-name')
]
