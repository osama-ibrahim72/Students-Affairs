from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')

def prepage(request):
    return render(request, 'pages/prepage.html')


# Create your views here.
