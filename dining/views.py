from django.shortcuts import render

def dining(request):
    return render(request, 'dining/dining.html')
