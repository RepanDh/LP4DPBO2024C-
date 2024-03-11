class Vehicle:
    __platNomor = ""
    __merk = ""
    __tahunProduksi = ""
    __warna = ""
    
    def __init__(self, platNomor = "", merk = "", tahunProduksi = "", warna = ""):
        self.__platNomor = platNomor
        self.__merk = merk 
        self.__tahunProduksi = tahunProduksi
        self.__warna = warna

    def get_platNomor(self):
        return self.__platNomor

    def set_platNomor(self, value):
        self.__platNomor = value

    def get_merk(self):
        return self.__merk

    def set_merk(self, value):
        self.__merk = value

    def get_tahunProduksi(self):
        return self.__tahunProduksi
    
    def set_tahunProduksi(self, value):
        self.__tahunProduksi = value

    def get_warna(self):
        return self.__warna

    def set_warna(self, value):
        self.__warna = value

    