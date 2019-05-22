from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        'name' : "Nina",
        'email' : "nina@gmail.com"
    }
    # Join.objects.create(owner_id=1, pet_id=1)
    return render(request, 'myapp/index.html', context)

def create_pet(request):
    # print('inside create_pet in views.py')
    # print("passing form to validate_pet_info method")
    errors = Pet.objects.validate_pet_info(request.POST)
    # print("inside create_pet in views.py again")
    # print(errors)

    if len(errors) > 0:
        # transfer error messages to "flash" messages
        for key, value in errors.items():
            messages.error(request, value)
        # redirect to form to resubmit information
        return redirect("/")
    else:
        # passed validation
        # create pet
        # save pet's id in session
        # redirect to success page
        return redirect("/success")

def success(request):
    return render(request, 'myapp/success.html')

def name(request, name):
    context = {
        'name' : name,
        'email' : f"{name}@gmail.com"
    }
    return render(request, 'myapp/index.html', context)
