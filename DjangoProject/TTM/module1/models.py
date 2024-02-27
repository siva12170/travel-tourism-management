from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.PositiveIntegerField()

    class Meta:
        db_table = "Register"


class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key=True)
    comment = models.TextField(max_length=255)

    class Meta:
        db_table = 'contactus'
