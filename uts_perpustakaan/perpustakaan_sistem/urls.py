from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter 

from data.views import BukuViewSet, AnggotaViewSet, PeminjamanViewSet 

router = DefaultRouter()

router.register(r'bukudrf', BukuViewSet)
router.register(r'anggotadrf', AnggotaViewSet)
router.register(r'peminjamandrf', PeminjamanViewSet) 


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('data.urls')), 
    
    path('api/', include(router.urls)), 
    
    path('api/', include('data.api_urls')),
]