from django.shortcuts import render

def index(request):
    context = {
        'name' : "Nina",
        'email' : "nina@gmail.com"
    }
    return render(request, 'myapp/index.html', context)

def success(request):
    return render(request, 'myapp/success.html')

def name(request, name):
    context = {
        'name' : name,
        'email' : f"{name}@gmail.com"
    }
    return render(request, 'myapp/index.html', context)
