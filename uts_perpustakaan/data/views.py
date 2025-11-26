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


from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import BukuSerializer, AnggotaSerializer, PeminjamanSerializer



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
    fields = ['nomor_anggota', 'nama_lengkap', 'alamat']
    success_url = reverse_lazy('anggota-list')

class AnggotaUpdateView(UpdateView):
    model = Anggota
    fields = ['nomor_anggota', 'nama_lengkap', 'alamat']
    
    def get_success_url(self):
        return reverse_lazy('anggota-detail', kwargs={'pk': self.object.pk})

class AnggotaDeleteView(DeleteView):
    model = Anggota
    success_url = reverse_lazy('anggota-list')

class PeminjamanListView(ListView):
    model = Peminjaman


class BukuListAPIView(ListAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class BukuDetailAPIView(RetrieveAPIView):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
    
    

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
    
class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer
    
class PeminjamanViewSet(viewsets.ModelViewSet):
    queryset = Peminjaman.objects.all()
    serializer_class = PeminjamanSerializer