from django.shortcuts import render


def mylist(request):
    return render(request, 'shopping_list.html')


def mytest(request):
    if request.method == 'POST':
        print('receivedData: ', request.POST['itemName']) #daten vom frontend zum Backend Übergeben
    if request.method == 'GET':
        print('Data sent: ') #daten vom frontend zum Backend Übergeben
    return render(request, 'test.html')
