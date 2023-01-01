from django.shortcuts import render
from django.views import View

from .models import HighScore

class Asteroid(View):
    def get(self, request):
        context = {}
        context['high_scores'] = HighScore.objects.order_by("-score")[:10]
        return render(request, 'asteroid/index.html', context)
