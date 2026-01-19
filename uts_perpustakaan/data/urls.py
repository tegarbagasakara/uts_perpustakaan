from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularSwaggerView, 
    SpectacularRedocView
)
from .views import (
    IndexView, BukuViewSet, AnggotaViewSet, PeminjamanViewSet,
    BukuListView, BukuDetailView, BukuCreateView, BukuUpdateView, BukuDeleteView,
    AnggotaListView, AnggotaDetailView, AnggotaCreateView, AnggotaUpdateView, AnggotaDeleteView,
    PeminjamanListView, PeminjamanCreateView, PeminjamanDetailView, PeminjamanUpdateView, PeminjamanDeleteView,
)

# Buat Router untuk API
router = DefaultRouter()
router.register(r'buku', BukuViewSet, basename='api-buku')
router.register(r'anggota', AnggotaViewSet, basename='api-anggota')
router.register(r'peminjaman', PeminjamanViewSet, basename='api-peminjaman')

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
    
    # URL HTML (Web Biasa)
    path('web/buku/', BukuListView.as_view(), name='buku-list'),
    path('web/buku/create/', BukuCreateView.as_view(), name='buku-create'),
    path('web/buku/<int:pk>/', BukuDetailView.as_view(), name='buku-detail'),
    path('web/anggota/', AnggotaListView.as_view(), name='anggota-list'),
    path('web/peminjaman/', PeminjamanListView.as_view(), name='peminjaman-list'),

    # URL API (Hasil Router)
    path('api/', include(router.urls)),
    
    # Path Dokumentasi UAS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]