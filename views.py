from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View

from .models import HighScore

class Asteroid(View):
    def get(self, request):
        context = {}
        context['high_scores'] = HighScore.objects.order_by("-score")[:10]
        return render(request, 'asteroid/index.html', context)

    def post(self, request):
        highscore = HighScore()
        highscore.date = date.today()
        highscore.name = request.POST["name"]
        highscore.score = request.POST["score"]
        highscore.save()
        return HttpResponseRedirect(reverse('asteroid:index'))
