from Buku.models import daftar_buku


def run_view():
    print ("Daftar Teman:")
    print ("---")

    for dbk in daftar_buku:
        print (dbk)