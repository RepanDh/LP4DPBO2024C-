from Vehicle import Vehicle

class Motorcycle(Vehicle):
    __jenisMotor = ""
    __kapasitasTangki = ''
    
    def __init__(self,platNomor = "", merk = "", tahunProduksi = "", warna = "", jenisMotor = "", kapasitasTangki = ''):
        super().__init__(platNomor, merk, tahunProduksi, warna)
        self.__jenisMotor = jenisMotor
        self.__kapasitasTangki = kapasitasTangki
    

    def get_jenisMotor(self):
        return self.__jenisMotor

    def set_jenisMotor(self, value):
        self.__jenisMotor = value

    def get_kapasitasTangki(self):
        return self.__kapasitasTangki

    def set_kapasitasTangki(self, value):
        self.__kapasitasTangki = value

    