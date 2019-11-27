from django.shortcuts import render, redirect
from .models import *
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TelefonForm, EmailForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.


class IndexView(TemplateView):
    template_name = 'phonebook_app/index.html'


class OsobaIndexView(ListView):
    context_object_name = 'people_list'
    model = Osoba
    template_name = 'phonebook_app/index.html'


class OsobaDetailView(DetailView):
    context_object_name = 'people_detail'
    model = Osoba
    template_name = 'phonebook_app/person_detail.html'



class OsobaCreateView(CreateView):
    fields = ('imie', 'nazwisko')
    model = Osoba
    template_name = 'phonebook_app/person_form.html'


class OsobaUpdateView(UpdateView):
    fields = ('imie', 'nazwisko')
    model = Osoba
    template_name = 'phonebook_app/person_form.html'


class OsobaDeleteView(DeleteView):
    model = Osoba
    success_url = reverse_lazy("list")


class TelefonFormView(CreateView):
    template_name = 'phonebook_app/add_phone.html'

    def get(self, request,  pk):
        form = TelefonForm()
        telefon = Telefon.objects.all()

        args = {
            'form': form, 'telefony': telefon
        }
        return render(request, self.template_name, args)

    def post(self, request, pk):
        osoba = get_object_or_404(Osoba, pk=pk)
        form = TelefonForm(data=request.POST)
        if form.is_valid():
            telefon = form.save(commit=False)
            telefon.osoba = osoba
            telefon.save()
            return redirect('people_detail', pk=osoba.pk)

        else:
            return render(request, 'phonebook_app/index.html', {'form': form})

        args = {'form': form}
        return render(request, self.template_name, args)


class EmailFormView(CreateView):
    template_name = 'phonebook_app/add_email.html'

    def get(self, request,  pk):
        form = EmailForm()
        email = Email.objects.all()

        args = {
            'form': form, 'emaile': email
        }
        return render(request, self.template_name, args)

    def post(self, request, pk):
        osoba = get_object_or_404(Osoba, pk=pk)
        form = EmailForm(data=request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.osoba = osoba
            email.save()
            return redirect('people_detail', pk=osoba.pk)

        else:
            return render(request, 'phonebook_app/index.html', {'form': form})

        args = {'form': form}
        return render(request, self.template_name, args)


class SearchView(ListView):
    template_name = 'phonebook_app/search.html'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        telephone = []
        e_mail = []
        request = self.request
        query = request.GET.get('q')
        if query:
            imie_results = Osoba.objects.filter(Q(imie__icontains=query))
            nazwisko_results = Osoba.objects.filter(Q(nazwisko__icontains=query))
            telefon_results = Telefon.objects.filter(Q(telefon__icontains=query))
            email_results = Email.objects.filter(Q(email__icontains=query))

            if telefon_results:
                for i in range(len(telefon_results)):
                    tel = telefon_results[i].telefon
                    telephone.append(get_object_or_404(Osoba, id=Telefon.objects.get(telefon=tel).osoba.id))
                return telephone

            if email_results:
                for i in range(len(email_results)):
                    mail = email_results[i].email
                    e_mail.append(get_object_or_404(Osoba, id=Email.objects.get(email=mail).osoba.id))
                return e_mail

            qs = imie_results or nazwisko_results or telephone or e_mail

            return qs
        return Osoba.objects.all()
