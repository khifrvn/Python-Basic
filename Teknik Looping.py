# Teknik Looping

nama_band = ['Weird Genius',
             'Fourtwnty',
             'Payung Teduh',
             'One Direction',
             'Senar Senja']

kumpulanLagu = ['WKWKLand',
        'Akad',
        'Zona Nyaman',
        'Perfect',
        'Dialog Hujan']

# ENUMERATE = mereturn indeks

for i, band in enumerate(nama_band):
    print(i, ':', band)

# ZIP = menggabungkan list.

for band, lagu in zip(nama_band, kumpulanLagu):
    print(band, 'lagunya', lagu)

# SORTED = mementukan urutan
playlist = {'Kopi dini hari', 'siang hari', 'pagi malam', 'lofi'}

for lagu in sorted (playlist):
    print(lagu)
print(10*"=")

# DICTIONARY = mirip dengan zip

playlist2 = {'Weird Genius': 'WKWKLand',
             'Fourtwnty': 'Zona Nyaman',
             'Payung Teduh': 'Payung Teduh',
             'One Direction': 'Perfect',
             'Senar Senja': 'Dialog Hujan'}

for i,v in playlist2.items():
    print(i, "lagunya", v)
