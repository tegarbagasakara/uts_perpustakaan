from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    BukuViewSet, AnggotaViewSet, PeminjamanViewSet,
    BukuListAPIView, BukuDetailAPIView 
)

router = DefaultRouter()
router.register(r'buku-crud', BukuViewSet)
router.register(r'anggota-crud', AnggotaViewSet)
router.register(r'peminjaman-crud', PeminjamanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('buku-read/', BukuListAPIView.as_view(), name='api-buku-list'),
    path('buku-read/<int:pk>/', BukuDetailAPIView.as_view(), name='api-buku-detail'),
]
