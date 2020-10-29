from django.shortcuts import render

# Create your views here.


def shoot(request):
    return render(request, 'camera/shot.html')
