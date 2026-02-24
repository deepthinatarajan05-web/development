from django.urls import path
from .views import students


urlpatterns = [
    path('ad/',students),
    path('ad/<int:id>/',students),
]