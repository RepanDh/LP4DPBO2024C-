from Vehicle import Vehicle

class ParkingLot:
    __kapasitas = ''
    __jumKendaraan = ''
    
    
    
    def __init__(self, kapasitas , jumKendaraan):
        self.__kapasitas = kapasitas
        self.__jumKendaraan = jumKendaraan
        self.__kendaraan = []
 
    def get_Kendaraan(self):
        return self.__kendaraan
    
    def set_Kendaraan(self, value):
        if not self.__kendaraan:  # Jika daftar kendaraan kosong
            self.__kendaraan.append(Vehicle(platNomor = "", merk= "", tahunProduksi= "", warna= ""))  # Tambahkan kendaraan kosong
        self.__kendaraan.append(value)  # Tambahkan kendaraan ke daftar

    def get_kapasitas(self):
        return self.__kapasitas

    def set_kapasitas(self, value):
        self.__kapasitas = value

    def get_jumKendaraan(self):
        return self.__jumKendaraan

    def set_jumKendaraan(self, value):
        self.__jumKendaraan = value

    