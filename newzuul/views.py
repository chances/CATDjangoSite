from django.shortcuts import render
from django.http import HttpResponse
from newzuul.models import consumer, items

# Create your views here.

from newzuul.models import consumer, items


def index(request):
    consumer_list = consumer.objects.order_by('name')
    context = {'consumer_list': consumer_list}
    return render(request, 'newzuul/index.html', context)
    return HttpResponse(output)