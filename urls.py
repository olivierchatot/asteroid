from django.urls import path
from asteroid.views import Asteroid

app_name="asteroid"
urlpatterns = [
    path('', Asteroid.as_view(), name="index"),
    path('save_high_score', Asteroid.as_view(), name="save_high_score"),
]
