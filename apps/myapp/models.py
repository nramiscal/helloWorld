from django.db import models

# Create your models here.
class PetManager(models.Manager):
    def validate_pet_info(self, form):

        # print("inside validate_pet_info method in models.py")
        # print("form is", form)

        errors = {}

        if len(form['name']) == 0:
            errors['name'] = "Name cannot be blank."
        elif len(form['name']) < 3:
            errors['name'] = "Name must be at least 3 characters."

        if len(form['species']) == 0:
            errors['species'] = "Species cannot be blank."

        if len(form['breed']) == 0:
            errors['breed'] = "Breed cannot be blank."

        if len(form['age']) == 0:
            errors['age'] = "Age cannot be blank."

        if len(form['password']) == 0:
            errors['password'] = "Password cannot be blank."

        return errors


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # pets --> joins to Pet class (ManyToMany)
    objects = models.Manager()

class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # owners = models.ManyToManyField(Owner, related_name="pets")

    # objects = models.Manager()
    objects = PetManager() #overwrites objects

class Join(models.Model):
    owner = models.ForeignKey(Pet, related_name="pets", on_delete=models.CASCADE)
    pet = models.ForeignKey(Owner, related_name="owners", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







# EOF
