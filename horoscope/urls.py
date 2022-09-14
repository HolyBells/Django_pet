from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index),
    path('<int:sign_zodiac>', views_horoscope.get_info_about_sign_zodiac_number),
    path('<str:sign_zodiac>', views_horoscope.get_info_about_sign_zodiac, name='horoscope-name')
]
