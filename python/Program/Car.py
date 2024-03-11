from Vehicle import Vehicle
class Car(Vehicle):
    __jumKursi = ''
    __jumPintu = ''

    def __init__(self, platNomor = "", merk = "", tahunProduksi = "", warna = "", jumKursi = '', jumPintu = ''):
        super().__init__(platNomor, merk , tahunProduksi , warna )
        self.__jumKursi = jumKursi
        self.__jumPintu = jumPintu

    def get_jumKursi(self):
        return self.__jumKursi

    def set_jumKursi(self, value):
        self.__jumKursi = value

    def get_jumPintu(self):
        return self.__jumPintu

    def set_jumPintu(self, value):
        self.__jumPintu = value

        
    