from django.db import models

class Anggota(models.Model):
    nomor_anggota = models.CharField(max_length=10, unique=True)
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return self.nama_lengkap

class Buku(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    tahun_terbit = models.IntegerField()
    jumlah_stok = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.judul

class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='riwayat_pinjam') 
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE, related_name='riwayat_pinjam') 
    tanggal_pinjam = models.DateField(auto_now_add=True) 
    tanggal_kembali = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.anggota.nama_lengkap} meminjam {self.buku.judul}"