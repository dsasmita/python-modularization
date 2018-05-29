class Buku:
    JUMLAH = 0

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = ''
        Buku.JUMLAH = Buku.JUMLAH + 1;

    def __str__(self):
        if self.tahun_terbit == '':
            return ("Judul = %s, Penulis = %s" %(self.judul, self.penulis))
        else:
            return ("Judul = %s, Penulis = %s, Tahun terbit = %s" %(self.judul, self.penulis, self.tahun_terbit))

    def dictionary(self):
        if self.tahun_terbit == '':
            return ("Judul Buku ini adalah %s yang ditulis oleh %s" %(self.judul, self.penulis))
        else:
            return ("Judul Buku ini adalah %s yang ditulis oleh %s terbit pada tahun %s" %(self.judul, self.penulis, self.tahun_terbit))

daftar_buku = []
daftar_buku.append(Buku("Manual Book Kipas", "Maspion"))

buku = Buku("Python Fundamental", "Mr Python")
buku.tahun_terbit = '2018'
dictionary = buku.dictionary()
print (dictionary)
daftar_buku.append(buku)
print ("")
print ("Jumlah Buku: %d" % buku.JUMLAH)
