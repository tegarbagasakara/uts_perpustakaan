from django import forms
from .models import Buku, Anggota 

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['isbn', 'judul', 'penulis', 'tahun_terbit'] 
        
        labels = {
            'isbn': 'Kode Buku', 
            'judul': 'Judul Buku',
            
        }
        
class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = ['nomor_anggota', 'nama_lengkap', 'alamat']

