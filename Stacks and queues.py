from collections import deque

antrian = deque([1,2,4,5,6,7])

#Nambah data
print('Data skrg: ', antrian)
antrian.append(9)

#menghapus data
print('Data skrg: ', antrian)
antrian.popleft()
print('Data skrg: ', antrian)




print("=" * 30)
tumpukan = [1,2,3,4,5,6]

# Ini append -===
tumpukan.append(7)
print(tumpukan)
# ===========----

# ---- Ini adalah teknik stacking
# untuk queue
print("Data sekarang: ", tumpukan)
tumpukan.pop() # ----> menghilangkan data paling belakang
print("Data sekarang: ", tumpukan)
print("="* 30)

