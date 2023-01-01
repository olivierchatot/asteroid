from django.urls import path
from asteroid.views import Asteroid

urlpatterns = [
    path('', Asteroid.as_view()),
]
