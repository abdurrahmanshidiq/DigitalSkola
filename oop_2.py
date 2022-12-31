class Binatang:
    nama_latin = 'Animalia'

    def __init__(self, nama, gender):
        self.nama = nama
        self.gender = gender

    @classmethod
    def tidur(cls):
        print(f"{cls.nama_latin} sedang tidur")

    @staticmethod
    def bangun():
        print(f"{Binatang.nama_latin} sudah bangun")

    def makan(self):
        print(f"{self.nama} sedang makan")

class Kucing(Binatang):
    pass

kucing = Kucing("Miki", "Jantan")
kucing.makan()