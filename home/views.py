from django.shortcuts import render

def index(request):
    """ A view to retunr index.html """
    return render(request, 'home/index.html')
