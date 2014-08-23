from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from newzuul.models import consumer, items


def index(request):
    return HttpResponse("hello world")