from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

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
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print(hashed_pw)
        pet = Pet.objects.create(name = request.POST['name'], species = request.POST['species'], breed = request.POST['breed'], age=request.POST['age'], password = hashed_pw.decode())  # <-- note the .decode()!!!

        # save pet's id in session
        request.session['pet_id'] = pet.id
        # redirect to success page
        return redirect("/success")

def success(request):
    context = {
        'pet' : Pet.objects.get(id = request.session['pet_id'])
    }
    return render(request, 'myapp/success.html', context)

def name(request, name):
    context = {
        'name' : name,
        'email' : f"{name}@gmail.com"
    }
    return render(request, 'myapp/index.html', context)
