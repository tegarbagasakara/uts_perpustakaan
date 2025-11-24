from django.views.generic import ListView, TemplateView 
from .models import Buku, Anggota



class BukuListView(ListView):
    model = Buku 

class AnggotaListView(ListView):
    model = Anggota

class IndexView(TemplateView):
    template_name = 'data/index.html'