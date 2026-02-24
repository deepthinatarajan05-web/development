
from django.urls import path
from .views import studentlist

urlpatterns = [
    path('ad/',studentlist),
    path('ad/<int:id>/',studentlist),
]