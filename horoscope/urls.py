from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index),
    path('type', views_horoscope.types),
    path('type/<str:elements>', views_horoscope.element, name='horoscope_elements'),
    path('<int:sign_zodiac>', views_horoscope.get_info_about_sign_zodiac_number),
    path('<str:sign_zodiac>', views_horoscope.get_info_about_sign_zodiac, name='horoscope-name')
]
