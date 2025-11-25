from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.urls import reverse_lazy 
from .models import Buku, Anggota, Peminjaman
from .forms import BukuForm, AnggotaForm 


class IndexView(TemplateView):
    template_name = 'data/index.html'

class BukuListView(ListView):
    model = Buku

class BukuDetailView(DetailView):
    model = Buku

class BukuCreateView(CreateView):
    model = Buku
    form_class = BukuForm 
    success_url = reverse_lazy('buku-list')

class BukuUpdateView(UpdateView):
    model = Buku
    fields = ['isbn', 'judul', 'penulis', 'tahun_terbit']

    def get_success_url(self):
        return reverse_lazy('buku-detail', kwargs={'pk': self.object.pk})

class BukuDeleteView(DeleteView):
    model = Buku
    success_url = reverse_lazy('buku-list')

class AnggotaListView(ListView):
    model = Anggota

class AnggotaDetailView(DetailView): 
    model = Anggota

class AnggotaCreateView(CreateView):
    model = Anggota
    form_class = AnggotaForm 
    success_url = reverse_lazy('anggota-list')

class AnggotaUpdateView(UpdateView):
    model = Anggota
    form_class = AnggotaForm
    success_url = reverse_lazy('anggota-detail')

class AnggotaDeleteView(DeleteView):
    model = Anggota
    success_url = reverse_lazy('anggota-list')

class PeminjamanListView(ListView):
    model = Peminjaman
