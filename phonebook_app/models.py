from django.db import models
from django.urls import reverse
# Create your models here.


class Osoba(models.Model):
    imie = models.CharField(max_length=50)

    nazwisko = models.CharField(max_length=50)


    def __str__(self):
        self.osoba = self.imie + " " + self.nazwisko
        return self.osoba

    def get_absolute_url(self):
        return reverse("people_detail", kwargs={"pk": self.pk})


class Telefon(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False, on_delete=models.CASCADE)

    telefon = models.CharField(max_length=50)


    def __str__(self):
        return self.telefon


class Email(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False, on_delete=models.CASCADE)

    email = models.EmailField()


    def __str__(self):
        return self.email
