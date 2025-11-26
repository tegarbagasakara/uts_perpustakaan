from django.urls import path
from . import views
from .views import (
    IndexView, 
    BukuListView, BukuDetailView, BukuCreateView, BukuUpdateView, BukuDeleteView,
    AnggotaListView, AnggotaDetailView, AnggotaCreateView, AnggotaUpdateView, AnggotaDeleteView,
    PeminjamanListView 
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 

    path('buku/', BukuListView.as_view(), name='buku-list'),
    path('buku/create/', BukuCreateView.as_view(), name='buku-create'),
    path('buku/<int:pk>/', BukuDetailView.as_view(), name='buku-detail'),
    path('buku/<int:pk>/update/', BukuUpdateView.as_view(), name='buku-update'),
    path('buku/<int:pk>/delete/', BukuDeleteView.as_view(), name='buku-delete'),
    
    path('anggota/', AnggotaListView.as_view(), name='anggota-list'),
    path('anggota/create/', AnggotaCreateView.as_view(), name='anggota-create'),
    path('anggota/<int:pk>/', AnggotaDetailView.as_view(), name='anggota-detail'),
    path('anggota/<int:pk>/update/', AnggotaUpdateView.as_view(), name='anggota-update'),
    path('anggota/<int:pk>/delete/', AnggotaDeleteView.as_view(), name='anggota-delete'),
    path('peminjaman/', PeminjamanListView.as_view(), name='peminjaman-list'),
    path('api/buku/', views.buku_list_api, name='buku-list-api'),
]