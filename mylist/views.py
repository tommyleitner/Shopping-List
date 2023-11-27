from django.shortcuts import render, redirect
from .models import ShoppingItem


def mylist(request):
    return render(request, 'shopping_list.html')


def mytest(request):
    if request.method == 'POST':
        print('receivedData: ', request.POST['itemName']) #daten vom frontend zum Backend Übergeben
        ShoppingItem.objects.create(name = request.POST['itemName'])
    if request.method == 'GET':
        print('Data sent: ')
    all_items = ShoppingItem.objects.all()
    #print(f"items: {repr(all_items)}")
    return render(request, 'test.html', {'all_items': all_items})
    
