from django.shortcuts import render

def index(request):
   return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def handler404(request,exception=None):
   return render(request, 'errors/404.html', {'error':exception}, status=404)


def handler505(request,exception=None):
   return render(request, 'errors/505.html', {'error':exception}, status=505)