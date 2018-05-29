class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = 2018

    def __str__(self):
        return ("Buku ini ber judul %s, dengan penulis %s" %(self.judul, self.penulis))

daftar_buku = []
buku = Buku("Manual Book Kipas", "Maspion")
daftar_buku.append(buku)

buku = Buku("Python Fundamental", "Mr Python")
daftar_buku.append(buku)
