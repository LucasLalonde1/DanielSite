from django.urls import path, include

from . import views

app_name = 'base'


urlpatterns = [
    path('', views.index, name="index"),
    path('portfolio/', views.portfolio, name='portfolio'),
    ]


