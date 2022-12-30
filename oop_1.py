class Kendaraan():
    # class attribute
    bahan_bakar = 'bensin'

    def __init__(self, nama, warna, jml_roda):
        self.nama = nama
        self.warna = warna
        self.jml_roda = jml_roda

    def maju(self):
        print(f"{self.nama} dengan warna {self.warna} dan jumlah roda {self.jml_roda} sedang maju")

    def mundur(self):
        print(f"{self.nama} dengan warna {self.warna} dan jumlah roda {self.jml_roda} sedang mundur")


# definisikan/ initiate sebuah object
mobil = Kendaraan('Mobil','Hitam','4')
motor = Kendaraan('Motor','Merah','3')

print('========Attribute========')
print(mobil.warna)
print(motor.warna)

print('==========Method=========')
mobil.maju()
motor.mundur()

# panggil class attribut
print('=====Class Attribute=====')
print(Kendaraan.bahan_bakar)
