from django.urls import path
from .views import BukuListView, AnggotaListView, IndexView 

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'), 
    
    
    path('buku/', BukuListView.as_view(), name='buku-list'),
    
    
    path('anggota/', AnggotaListView.as_view(), name='anggota-list'),
]