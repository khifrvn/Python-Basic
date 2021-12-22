names = ['John', 'Alex', 'Mosh', 'Rooney', 'Bob']
names[0] = 'Dany' # for updated some list

print(names[0])
print(names[-1])
print(names[2:])
print(names[2:-1])

print("="*30)

# ---- WRITE PROGRAM TO FIND THE LARGEST NUMBER IN A LIST ----

numbers = [1, 5, 8, 2, 15]

print("Largest number is : ", max(numbers))

# or

max = numbers [0]
for number in numbers:
    if number > max:
        max = number
print("Largest number is : ", max)

print("="*30)

# ------ 2D LIST ---------
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[0]
print(matrix[2][1])
print("===")

#for row in matrix:
 #   for item in row:
  #      print(item)

# -------------- LIST METHOD ------------

nomer = [1,6,8,4,7,5,5]
nomer.append(10)  # method menambah item
nomer.insert(1, 10)  # menambah item lebih spesific
nomer.remove(4)  # menghapus item
# nomer.clear()  # menghapus semua item
nomer.pop()  # menghapus item akhir
print(nomer)
print(nomer.index(1)) # mengetahui letak item
print(nomer.count(5)) # menghitung item yang sama

print("="*30)

# ==== How remove some duplicate item on list ====
kode = ['a','b','c','d','e','a','a']

kode = list(dict.fromkeys(kode))
print(kode)
print("==============")

# ==============================

hobi = []
stop = False
i = 0

while not stop:
    hobiBaru = input("ISI HOBI ANDA : ").format(i)
    hobi.append((hobiBaru))
    i += 1

    tanya = input("Mau isi lagi ? (y/t) : ")
    if tanya == "t":
        stop = True
print("=" *  10)
print("Kamu memiliki {} hobi".format(len(hobi)))
for hb in hobi:
    print("- {}".format(hb))


