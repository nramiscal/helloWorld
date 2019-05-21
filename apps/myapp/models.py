from django.db import models

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # pets --> joins to Pet class (ManyToMany)
    # objects = models.Manager()

class Pet(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # owners = models.ManyToManyField(Owner, related_name="pets")

    # objects = models.Manager()

class Join(models.Model):
    owner = models.ForeignKey(Pet, related_name="pets", on_delete=models.CASCADE)
    pet = models.ForeignKey(Owner, related_name="owners", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





# amsnm,
