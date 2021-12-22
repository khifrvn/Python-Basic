# TUPLE --> Tidak akan bisa diubah nilai item nya

tuple_tandaKurung = (1234, 5678, "hello")  # -----> lebih efektif
# atau bisa
tuple_tanpaKurung = 1234,768, 'hello'  # ---- > tanpa tanda kurung

print(tuple_tanpaKurung)
print("="*20)
# membuat tuple kosong

kosong = ()

# membuat singleton atau tuple satu saja

satu = ('isinya satu',)
satuTuple = 'isinya satu',

# memotong tuple

web = (123, 'Flaticon.com', 'https://www.facebook.com')

print(web[1:3])
print("="*20)

    # unpacking tuple

id_web, nama, url, = web
print(id_web)
print(nama)
print(url)
print("="*20)
# mengambil panjang tuple

hari = ('senin', 'selasa', 'rabu', 'kamis', 'jumat','sabtu','minggu')

print("Panjang hari adalah ", len(hari))
print("="*20)
# tuple nested

tuple1 = ("aku", "cinta", "kamu")
tuple2 = ("selama", 3, "tahun")
tuple3 = (tuple1, tuple2)   # ---> nested tuple

print(tuple3)
print("="*20)

 #unpacking
coordinates = (1,2,3)

x, y, z = coordinates

print(x)
print(y)
print(z)