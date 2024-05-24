from django.shortcuts import render

def retail(request):
    return render(request, 'retail/retail.html')
