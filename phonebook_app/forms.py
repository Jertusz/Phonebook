from django.forms import ModelForm, CharField
from .models import Telefon, Email


class TelefonForm(ModelForm):
    telefon = CharField()

    class Meta:
        model = Telefon
        fields = ("telefon",)


class EmailForm(ModelForm):
    email = CharField()

    class Meta:
        model = Email
        fields = ("email",)
