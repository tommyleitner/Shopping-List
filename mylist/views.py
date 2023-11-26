from django.shortcuts import render


def mylist(request):
    return render(request, 'shopping_list.html')


def mytest(request):
    if request.method == 'POST':
        print('receivedData: ', request.POST['itemName'])
    return render(request, 'test.html')
