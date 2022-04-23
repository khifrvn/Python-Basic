# class
class mahasiswa():
    # nama = 'nama'  # ------> attribut

    # untuk nilai default simpan disini
    __nilai = 0  # -------> Double __ (underscroe) berfungsi untuk private
    __jurusan = "Teknik informatika"

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim  # public

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def checkStatus(self):
        if self.__nilai <= 50:
            print(self.nama, 'Anda tidak lulus')
        else:
            print(self.nama, 'Lulus')



# main program
# main program
otong = mahasiswa("Otong Surotong", 13332221)  #  ------> otong adalah mahasiswa (OBJEK)
ucup = mahasiswa("Ucup kucup", 23332221)

otong.uts(10)
otong.uas(50)

otong.checkStatus()

ucup.uts(0)
ucup.uas(25)

ucup.checkStatus()

print()
