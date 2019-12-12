
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.getAll, name='getAll'),
    path('import/', views.importTwenty),
    path('fight/<int:id1>/<int:id2>/', views.fight)
]
