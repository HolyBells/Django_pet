from django.urls import path
from . import views as views_geometry


urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views_geometry.get_rectangle_area, name='rectangle_url'),
    path('square/<int:side>', views_geometry.get_square_area, name='square_url'),
    path('circle/<int:radius>', views_geometry.get_circle_area, name='circle_url'),
    path('get_rectangle_area/<int:width>/<int:height>', views_geometry.get_rectangle_area_redirect),
    path('get_square_area/<int:width>', views_geometry.get_square_area_redirect),
    path('get_circle_area/<int:radius>', views_geometry.get_circle_area_redirect),

]
