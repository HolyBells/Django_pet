from django.urls import path
from . import views as views_blog

urlpatterns = [
    path('', views_blog.index),
    path('kianu', views_blog.kianu),
]