
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.getAll, name='getAll'),
    path('import/', views.importAll),
    path('fight/<int:id1>/<int:id2>/', views.fight),
    path('purge', views.purge)
]
