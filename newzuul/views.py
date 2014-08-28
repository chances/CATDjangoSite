from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from newzuul.models import consumer, items

# Create your views here.


def purchase_item(person, item_id, ammount):
    try:
        item = get_object_or_404(items, pk=item_id)
    except (ValueError):
        return False
    else:
        person.bank -= item.price * int(ammount)
        person.save()
        return True


def index(request):
    consumer_list = consumer.objects.order_by('name')
    item_list = items.objects.order_by('price')
    context = {'consumer_list': consumer_list,
               'item_list': item_list}
    return render(request, 'newzuul/index.html', context)


def purchaselist(request, user_id):
    person = get_object_or_404(consumer, pk=user_id)
    item_list = items.objects.order_by('price')
    context = {'item_list': item_list, 'person': person}
    return render(request, 'newzuul/purchaselist.html', context)


def purchaseaction(request, user_id):
    person = get_object_or_404(consumer, pk=user_id)

    for key in request.POST:
        purchase_item(person, key, request.POST[key])

    return HttpResponse('did it!')
    #return redirect('newzuul:purchaselist.html')