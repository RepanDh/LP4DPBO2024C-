from Vehicle import Vehicle

class Garage:
    __namaGarasi = ""
    __luasGarasi = ''
    
    
    def __init__(self, namaGarasi="", luasGarasi=0):
        self.__namaGarasi = namaGarasi
        self.__luasGarasi = luasGarasi
        self.__kendaraan = []


    def get_namaGarasi(self):
        return self.__namaGarasi

    def set_namaGarasi(self, namaGarasi):
        self.__namaGarasi = namaGarasi

    def get_luasGarasi(self):
        return self.__luasGarasi

    def set_luasGarasi(self, luasGarasi):
        self.__luasGarasi = luasGarasi

    def get_Kendaraan(self):
        return self.__kendaraan

    def set_Kendaraan(self, value):
        if not self.__kendaraan:  # Jika daftar kendaraan kosong
            self.__kendaraan.append(Vehicle(platNomor = "", merk= "", tahunProduksi= "", warna= ""))  # Tambahkan kendaraan kosong
        self.__kendaraan.append(value)  # Tambahkan kendaraan ke daftar

