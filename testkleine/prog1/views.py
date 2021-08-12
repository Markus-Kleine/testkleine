from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic.list import ListView
from django.views.generic import ListView
from prog1.forms import Person, ArtikelForm
from prog1.models import PersonModell, Artikel
import requests
from prog1.api import CocktailAPI, ArtdetAPI

# Create your views here.
# Startseite für http://localhost:8000/prog1/
def home(request):
    return render(request, "base.html")

def test(request):
    data={'name':'otto','alter':24}
    data["personen_form"] = Person()
    data["artikel_form"] = ArtikelForm()
    return render(request, "prog1/test.html", data)

def create(request):
    lv_first = request.POST.get("first_name")
    lv_last = request.POST.get("last_name")
    new_person = PersonModell(first_name=lv_first,last_name=lv_last)
    new_person.save()
    return HttpResponse("Nutzer  " + new_person.first_name + new_person.last_name + " wurde erstellt")

def user_list(request):
    users = PersonModell.objects.all()
    filter_users = PersonModell.objects.filter(last_name__icontains='Ga')
    cocktailapi = CocktailAPI()
    wert = cocktailapi.get_cocktails('margarita')
    data = {'users':users, 'user_filtered':filter_users, 'cocktails': wert}
    return render(request, "prog1/liste.html", data)

def createartikel(request):
    new_artikel = ArtikelForm(request.POST,request.FILES)
    if new_artikel.is_valid():
        ls_artikel = Artikel()
        ls_artikel.matnr = new_artikel.cleaned_data['matnr']
        ls_artikel.maktx_1 = new_artikel.cleaned_data['maktx_1']
        ls_artikel.maktx_2 = new_artikel.cleaned_data['maktx_2']
        ls_artikel.lifnr   = new_artikel.cleaned_data['lifnr']
#        ls_artikel.artikelbild = new_artikel.cleaned_data['artikelbild']
        ls_artikel.save()
#        value = new_artikel.cleaned_data
#        artikel = Artikel(value)
#        artikel.save()
        return HttpResponse("Artikel  " + str(ls_artikel.matnr) + " wurde erstellt")
    else:
        print("Fehler")
        return HttpResponse("Fehler " + str(new_artikel.errors))

class ArtikelListView(ListView):
    model = Artikel

def artikel_detail(request):
    artdetapi = ArtdetAPI()
    data = artdetapi.get_artikel('410460')
    return render(request, "prog1/artikel_detail.html", data)