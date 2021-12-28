from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('vote/<str:pk>', views.vote, name='vote'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('results/<str:pk>', views.results, name='results'),
]