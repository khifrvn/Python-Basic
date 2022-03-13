# cara membuat fungsi

def nama_fungsi(): # ---> ini adalah contoh fungsi
    print("Hello World !")
    print("=" * 10)

# cara memanggil fungsi
nama_fungsi()

# fungsi dengan parameter

def salam(ucapan):
    print(ucapan)

salam("Selamat pagi !")
print("=" * 10)
     # apabila lebih dari satu parameter


def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga : ", luas)

luas_segitiga(4, 3)

    # Menggunakan return untuk mengembalikan nilai

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# Print 
print("luas persegi : ", luas_persegi(5))

def volume_persegi(sisi):
    volume = luas_persegi(sisi)*sisi
    return volume

print("Volume Persegi : ", volume_persegi(5))
print("=" * 10)

# --------- Variabel Global dan lokal ------

    # ini varibael global
nama = "Majalah"
versi = "1.0.0"

def var_lokal():
    # ini variabel lokal
    nama = "Program"
    versi = "1.2.0"
    # mengakses variabel lokal
    print("Nama: ", nama)
    print("Versi: ", versi)

    # mengakses variabel global
print("Nama : ", nama)
print("Versi : ", versi)
    # memanggil variabel lokal
var_lokal()

print("=" * 20)

def nama_barang(nama, harga, fungsi):
    print("Nama barang : ", nama)
    print("Harga barang : ", harga)
    print("Fungsi Barang : ", fungsi)

# ---- keyword arguments -----
nama_barang(nama="Mouse", harga="200K", fungsi="Pointing device")
nama_barang(nama="Keyboard", harga="300K", fungsi="Type any word")
print("="*20)


# ----- LAMBDA FUCTION -----

def jumlah(a, b):
    c= a+b
    return c
hasil = jumlah(4,4)
print(hasil)

    # membuat anonymous function dgn lambda

perkalian = lambda item1, item2: item1*item2
hasil = perkalian(30, 10)
print(hasil)
