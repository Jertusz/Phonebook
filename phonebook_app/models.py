from django.db import models

# Create your models here.


class Osoba(models.Model):
    imie = models.CharField(max_length=50)

    nazwisko = models.CharField(max_length=50)


class Telefon(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False)

    telefon = models.CharField(max_length=50)


class Email(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False)

    email = models.EmailField()
