from django.shortcuts import render
from django.views import View

class Asteroid(View):
    def get(self, request):
        return render(request, 'asteroid/index.html')
