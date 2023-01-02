from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import View

from .models import HighScore

class Asteroid(View):
    def get(self, request):
        context = {}
        context['high_scores'] = HighScore.objects.order_by("-score")[:10]
        for index, score in enumerate(context['high_scores']):
            if index == 0: score.style = "color: #33DAFF; font-weight: bold; font-size: 30px;"
            elif index == 1: score.style = "color: #FFD700; font-weight: bold;"
            elif index == 2: score.style = "color: #C9C0BB; font-weight: bold;"
            elif index == 3: score.style = "color: #CD7F32; font-weight: bold;"
            else: score.style = "color: #000;"
        return render(request, 'asteroid/index.html', context)

    def post(self, request):
        highscore = HighScore()
        highscore.date = date.today()
        highscore.name = request.POST["name"]
        highscore.score = request.POST["score"]
        highscore.save()
        return HttpResponseRedirect(reverse('asteroid:index'))
