from django.urls import path

from . import views

app_name = 'ildb'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
]
