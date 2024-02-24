
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('details/<int:id>', views.details, name='details'),
]