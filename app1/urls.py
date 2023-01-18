from django.urls import path
from .views import hello_world, welcome




urlpatterns = [
    path("", hello_world),
    path("welcome/", welcome)

]