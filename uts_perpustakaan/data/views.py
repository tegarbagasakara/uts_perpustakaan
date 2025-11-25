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


class IndexView(TemplateView):
    template_name = 'data/index.html'

class BukuListView(ListView):
    model = Buku

class BukuDetailView(DetailView):
    model = Buku

class BukuCreateView(CreateView):
    model = Buku
    fields = ['isbn', 'judul', 'penulis', 'tahun_terbit']
    success_url = reverse_lazy('buku-list') 

class BukuUpdateView(UpdateView):
    model = Buku
    fields = ['isbn', 'judul', 'penulis', 'tahun_terbit']
    success_url = reverse_lazy('buku-detail') 
    
class BukuDeleteView(DeleteView):
    model = Buku
    success_url = reverse_lazy('buku-list') 
    
class AnggotaListView(ListView):
    model = Anggota

class AnggotaDetailView(DetailView):
    model = Anggota

class AnggotaCreateView(CreateView):
    model = Anggota
    fields = ['nomor_anggota', 'nama_lengkap', 'alamat']
    success_url = reverse_lazy('anggota-list')

class AnggotaUpdateView(UpdateView):
    model = Anggota
    fields = ['nomor_anggota', 'nama_lengkap', 'alamat']
    success_url = reverse_lazy('anggota-detail')
    

class AnggotaDeleteView(DeleteView):
    model = Anggota
    success_url = reverse_lazy('anggota-list')
    




class PeminjamanListView(ListView):
    model = Peminjaman
    