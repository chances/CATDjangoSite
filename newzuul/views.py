from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from newzuul.models import consumer, items
import json

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


def create_item(name_in, price_in):
    new_item = items(name=name_in, price=price_in)
    new_item.save()


def create_consumer(name_in, bank_in):
    new_consumer = consumer(name=name_in, bank=bank_in)
    new_consumer.save()


def index(request):
# show all people and all items (include banks and costs respectively)
    consumer_list = consumer.objects.order_by('name')
    item_list = items.objects.order_by('price')
    context = {'consumer_list': consumer_list,
               'item_list': item_list}
    return render(request, 'newzuul/index.html', context)


def purchaselist(request, user_id):
# purchaselist for person
    person = get_object_or_404(consumer, pk=user_id)
    item_list = items.objects.order_by('price')
    context = {'item_list': item_list, 'person': person}
    return render(request, 'newzuul/purchaselist.html', context)


def purchaseaction(request, user_id):
# action page for purchases, redirects to index
    try:
        person = get_object_or_404(consumer, pk=user_id)
    except (ValueError):
        return HttpResponse(" he's dead Jim (ValueError on person object)")
    else:
        for key in request:
            if key == "csrfmiddlewaretoken":
                continue
            elif purchase_item(person, key, request.POST[key]):
                continue
            else:
                #print exception error on webpage
                return HttpResponse('Hes dead Jim (purchase_item function ValueError)')
        #return HttpResponse('did it!')
        return redirect('newzuul:purchaselist.html')  # causes 400 error on runserver


def additemform(request):
    return render(request, 'newzuul/additemform.html')


def additemaction(request):
    if request.POST["keymastername"] == "zuulmaster" and request.POST["gatekeeperpassword"] == "onlyzuul":
        create_item(request.POST["new_item_name"], request.POST["new_item_price"])
        return redirect("newzuul:purchaselist.html")  # Still 400 on runserver; must test this out
    else:
        return HttpResponse("Something doesn't check out. I don't think 0.0you are the zuulmaster")


def adduserform(request):
    return render(request, 'newzuul/adduserform.html')


def adduseraction(request):
    create_consumer(request.POST["new_user_name"], request.POST["new_user_bank"])
    return redirect("newzuul:purchaselist.html")

# --- Verson 1 API below --- #


def v1purchase(request):
    returndict = {"success": "false", "name": "noname", "item": "noitem", "item_price": -1}
    name = request.POST["name"]
    purchase_me = request.POST["item"]
    person_id = -1
    item_id = -1

    # make lists
    consumer_list = consumer.objects.order_by('name')
    item_list = items.objects.order_by('name')

    # find person in db
    for person in consumer_list:
        if name == person.name:
            person_id = person.id
    if person_id >= 0:
        # set our buyer
        buyer = get_object_or_404(consumer, pk=person_id)

    # find item in db
    for item in item_list:
        if purchase_me == item.name:
            item_id = item.id
    if item_id >= 0:
        item_to_purchase = get_object_or_404(items, pk=item.id)

    if buyer and item_id >= 0:
        purchase_item(buyer, item_id, 1)  # so far will only purchase 1 of them; this may change later
        returndict["name"] = name
        returndict["item"] = purchase_me
        returndict["success"] = "true"
        returndict["item_price"] = str(item_to_purchase.price)

    returnjson = json.dumps(returndict)
    return HttpResponse(returnjson)

def v1checkballance(requets):
    return HttpResponse("you found me yaaaay!!!")