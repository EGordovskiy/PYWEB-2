from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from random import randint, random

class RandomView(View):
    def get(self, request):
        # random_number = random()
        randint_number = randint(10, 1000)
        return HttpResponse(randint_number)
