#Adhyaksa XI MIA 1/01#
class Siswa:
    '''Dasar kelas untuk semua siswa'''
    jumlah_siswa = 0

    def __init__(self, nama, hobi, umur):
        self.nama = nama
        self.hobi = hobi
        self.umur = umur
        Siswa.jumlah_siswa +=1

    def tampilkan_jumlah(self):
        print ("Total Siswa:", Siswa.jumlah_siswa)

    def tampilkan_hobi(self):
        print("Nama :", self.nama)
        print("Hobi :", self.hobi)
        print()

    def tampilkan_info_lengkap(self):
        print("Siswa bernama", self.nama, "yang berumur", self.umur, "memiliki hobi", self.hobi)

# Membuat objek pertama dari kelas Karyawan
siswa1 = Siswa("Jess", "Badminton", 17)

# Membuat objek pertama dari kelas Karyawan
siswa2 = Siswa("Krisna", "Bermain Gitar", 16)

siswa1.tampilkan_hobi()
siswa2.tampilkan_hobi()
siswa1.tampilkan_info_lengkap()
siswa2.tampilkan_info_lengkap()
print("Total Siswa:", Siswa.jumlah_siswa)
    
