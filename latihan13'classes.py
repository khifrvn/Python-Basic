# ======== THIS IS OOP DUDE !!! ========

class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 20
print(point2.x)

print("="*100)

# ==================================================

# class
class mahasiswa:
    # nama = 'nama'  # ------> attribut
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

    def belajar(self, kondisi):  # -----> Method/Function dalam class
        print(self.nama, 'Sedang belajar', kondisi)

    def tidur(self, kondisi):
        print(self.nama, 'Sedang tidur', kondisi)


# main program
otong = mahasiswa("Otong Surotong", 13332221)  #  ------> otong adalah mahasiswa (OBJEK)
ucup = mahasiswa("Ucup kucup", 23332221)

otong.belajar('dengan tekun')
ucup.tidur('di kelas')

print(otong.nim)
print(ucup.nim)


