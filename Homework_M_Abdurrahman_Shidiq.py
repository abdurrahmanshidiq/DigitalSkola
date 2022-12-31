# M. ABDURRAHMAN SHIDIQ 
# Data Engineer DigitalSkola, Week 2, Python III,
# 1. Buat class Hewan yang memiliki class attributes nama_latin dan instance attributes nama, warna, dan umur:  
#   a. Di class Hewan, memiliki instance method bangun, & makan
#   b. Buat child class Kucing yang memiliki value attribute nama_latin yang berbeda dengan class Hewan
#   c. Di child class, override method makan


class Hewan:
    nama_latin = 'Animalia'

    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    @classmethod
    def bagun(cls):
        print(f"{cls.nama_latin} sudah bangun")
        
    @staticmethod
    def makan():
        print(f"{Hewan.nama_latin} sedang makan")

class Kucing(Hewan):
    nama_latin = 'Felis'

    def makan(self):
        print(f"{self.nama} sedang makan ikan")

kucing = Kucing('Tom', 'Putih', 2)

kucing.bagun()
kucing.makan()