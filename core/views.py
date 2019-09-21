from django.shortcuts import render

def homepage_view(request):
    return render(request, 'core/homepage.html', {})

def index_view(request):
    return render(request, 'core/index.html')

