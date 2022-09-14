from django.urls import path
from . import views as views_geometry

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views_geometry.get_rectangle_area ),
    path('square/<int:side>', views_geometry.get_square_area ),
    path('circle/<int:radius>', views_geometry.get_circle_area ),
    path('get_rectangle_area/<int:width>/<int:height>', views_geometry.get_circle_area ),
    path('circle/<int:x>', views_geometry.get_circle_area ),
    path('circle/<int:x>', views_geometry.get_circle_area ),
]