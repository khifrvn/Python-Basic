# loop variabel

for item in range(5, 11) :
    print(item)

print("="*10)

gorengan = ['Tempe', 'Gehu', 'Combro', 'Tahu']
for grg in gorengan:
    print(grg)

#=================================================
i = 1
while i <= 5:
    print("*" * i)
    i += 1
#=================================================
print("="*30)

# for didalam for

buah = ['apel', 'jeruk', 'mangga', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

daftar_belanja = [gorengan, buah, sayur]

print(daftar_belanja)

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)
print("="*30)

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
