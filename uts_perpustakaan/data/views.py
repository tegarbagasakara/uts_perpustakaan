from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.utils import timezone

# --- IMPORT UNTUK DRF (PENTING!) ---
from rest_framework import viewsets, status, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# --- IMPORT MODEL & SERIALIZER (WAJIB ADA AGAR TIDAK NAMEERROR) ---
from .models import Buku, Anggota, Peminjaman 
from .serializers import BukuSerializer, AnggotaSerializer, PeminjamanSerializer

class IndexView(TemplateView):
    template_name = 'index.html'

# --- 1. Buku Views (HTML CRUD) ---
class BukuListView(ListView):
    model = Buku
    template_name = 'data/buku_list.html'
    context_object_name = 'buku_list'

class BukuDetailView(DetailView):
    model = Buku
    template_name = 'data/buku_detail.html'

class BukuCreateView(CreateView):
    model = Buku
    template_name = 'data/buku_form.html'
    fields = '__all__' 
    success_url = reverse_lazy('buku-list')

class BukuUpdateView(UpdateView):
    model = Buku
    template_name = 'data/buku_form.html'
    fields = '__all__'
    success_url = reverse_lazy('buku-list')

class BukuDeleteView(DeleteView):
    model = Buku
    template_name = 'data/buku_confirm_delete.html'
    success_url = reverse_lazy('buku-list')


# --- 2. Anggota Views (HTML CRUD) ---
class AnggotaListView(ListView):
    model = Anggota
    template_name = 'data/anggota_list.html'
    context_object_name = 'anggota_list'

class AnggotaDetailView(DetailView):
    model = Anggota
    template_name = 'data/anggota_detail.html'

class AnggotaCreateView(CreateView):
    model = Anggota
    template_name = 'data/anggota_form.html'
    fields = '__all__'
    success_url = reverse_lazy('anggota-list')

class AnggotaUpdateView(UpdateView):
    model = Anggota
    template_name = 'data/anggota_form.html'
    fields = '__all__'
    success_url = reverse_lazy('anggota-list')

class AnggotaDeleteView(DeleteView):
    model = Anggota
    template_name = 'data/anggota_confirm_delete.html'
    success_url = reverse_lazy('anggota-list')


# --- 3. Peminjaman Views (HTML CRUD) ---
class PeminjamanListView(ListView):
    model = Peminjaman
    template_name = 'data/peminjaman_list.html'
    context_object_name = 'peminjaman_list'

class PeminjamanCreateView(CreateView):
    model = Peminjaman
    template_name = 'data/peminjaman_form.html'
    fields = ['buku', 'anggota']  
    success_url = reverse_lazy('peminjaman-list')

class PeminjamanDetailView(DetailView):
    model = Peminjaman
    template_name = 'data/peminjaman_detail.html'
    
class PeminjamanUpdateView(UpdateView):
    model = Peminjaman
    template_name = 'data/peminjaman_form.html'
    fields = ['buku', 'anggota', 'tanggal_kembali']
    success_url = reverse_lazy('peminjaman-list')
    
class PeminjamanDeleteView(DeleteView):
    model = Peminjaman
    template_name = 'data/peminjaman_confirm_delete.html'
    success_url = reverse_lazy('peminjaman-list')


# --- 4. API ViewSets (Kriteria UAS Modul 13) ---

class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['judul', 'penulis'] 
    ordering_fields = ['judul', 'tahun_terbit']

class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer
    permission_classes = [IsStaffOrReadOnly]

class PeminjamanViewSet(viewsets.ModelViewSet):
    queryset = Peminjaman.objects.all()
    serializer_class = PeminjamanSerializer
    permission_classes = [IsStaffOrReadOnly]

    def perform_create(self, serializer):
        buku = serializer.validated_data['buku']
        if buku.jumlah_stok <= 0:
            raise ValidationError({"detail": "Gagal pinjam! Stok buku ini sudah habis (0)."})
        
        buku.jumlah_stok -= 1
        buku.save()
        serializer.save()

    @action(detail=True, methods=['post'])
    def kembalikan(self, request, pk=None):
        peminjaman = self.get_object()
        if peminjaman.tanggal_kembali:
            return Response({"detail": "Buku ini sudah dikembalikan sebelumnya."}, status=status.HTTP_400_BAD_REQUEST)

        peminjaman.tanggal_kembali = timezone.now()
        peminjaman.save()

        buku = peminjaman.buku
        buku.jumlah_stok += 1
        buku.save()

        return Response({"message": "Buku berhasil dikembalikan. Stok buku bertambah +1."}, status=status.HTTP_200_OK)