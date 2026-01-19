from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BukuViewSet, AnggotaViewSet, PeminjamanViewSet 

router = DefaultRouter()

router.register(r'buku', BukuViewSet, basename='api-buku')
router.register(r'anggota', AnggotaViewSet, basename='api-anggota') 
router.register(r'peminjaman', PeminjamanViewSet, basename='api-peminjaman') 

urlpatterns = [
    path('', include(router.urls)),
]