from rest_framework import serializers
from .models import Buku, Anggota, Peminjaman

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = ['id', 'isbn', 'judul', 'penulis', 'tahun_terbit']

class AnggotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anggota
        fields = '__all__'
        
class PeminjamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peminjaman
        fields = '__all__'