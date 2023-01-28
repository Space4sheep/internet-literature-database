from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    # Main page
    path('', views.index),
    path('results/', views.results),
    path('about/', views.about),
]
