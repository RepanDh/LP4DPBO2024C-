from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot
from Tabel import Table

# Membuat objek dari class Car dan Motorcycle
car1 = Car("B 1234 CD", "Toyota", "2023", "Red", 5, 4)
motor1 = Motorcycle("D 5678 EF", "Yamaha", "2024", "Blue", "Sport", 10)
car2 = Car("E 9101 GH", "Honda", "2022", "White", 4, 4)
motor2 = Motorcycle("F 1121 IJ", "Honda", "2023", "Black", "Matic", 5)
car3 = Car("AA 2345 JK", "Ford", "2024", "Blue", 4, 4)
motor3 = Motorcycle("H 6789 LM", "Suzuki", "2025", "Green", "Sport", 8)
car4 = Car("F 3456 NO", "Chevrolet", "2023", "Yellow", 5, 4)
motor4 = Motorcycle("J 7890 PQ", "Kawasaki", "2024", "Red", "Matic", 6)
car5 = Car("K 4567 RS", "Nissan", "2022", "Black", 4, 4)
motor5 = Motorcycle("L 8901 TU", "Harley", "2025", "White", "Sport", 10)
car6 = Car("L 5678 VW", "Hyundai", "2023", "Green", 5, 4)
motor6 = Motorcycle("N 9012 XY", "Ducati", "2024", "Blue", "Matic", 7)

# Membuat objek dari class Garage dan ParkingLot
garage1 = Garage("Garasi PA", 100)
parkinglot1 = ParkingLot(50, 0)

# Menambahkan kendaraan ke garasi
garage1.set_Kendaraan(car1)
garage1.set_Kendaraan(motor1)
garage1.set_Kendaraan(car2)
garage1.set_Kendaraan(motor2)
garage1.set_Kendaraan(car5)
garage1.set_Kendaraan(motor5)

# Menambahkan kendaraan ke parking lot
parkinglot1.set_Kendaraan(car3)
parkinglot1.set_Kendaraan(motor3)
parkinglot1.set_Kendaraan(car4)
parkinglot1.set_Kendaraan(motor4)
parkinglot1.set_Kendaraan(car6)
parkinglot1.set_Kendaraan(motor6)

# Menambahkan objek Car dan Motorcycle ke dalam daftar kendaraan
vehicles = [car1, motor1, car2, motor2, car3, motor3, car4, motor4, car5, motor5, car6, motor6]

# Membuat objek dari class Table
table = Table()

# Menyiapkan header dan konten tabel untuk garasi
garage_header = ["Plat Nomor", "Merk", "Tahun Produksi", "Warna", "Jenis Kendaraan"]
garage_content = [[v.get_platNomor(), v.get_merk(), v.get_tahunProduksi(), v.get_warna(), "Car" if isinstance(v, Car) else "Motorcycle"] for v in garage1.get_Kendaraan() if v.get_platNomor() or v.get_merk() or v.get_tahunProduksi() or v.get_warna()]

# print informasi kendaraan di garasi dalam bentuk tabel
print("Informasi Kendaraan di " + garage1.get_namaGarasi() + ":")
table.create_table(len(garage_content), len(garage_header), garage_content, garage_header)

# Menyiapkan header dan konten tabel untuk parking lot
parkinglot_header = ["Plat Nomor", "Merk", "Tahun Produksi", "Warna", "Jenis Kendaraan"]
parkinglot_content = [[v.get_platNomor(), v.get_merk(), v.get_tahunProduksi(), v.get_warna(), "Car" if isinstance(v, Car) else "Motorcycle"] for v in parkinglot1.get_Kendaraan() if v.get_platNomor() or v.get_merk() or v.get_tahunProduksi() or v.get_warna()]

# print informasi kendaraan di parking lot dalam bentuk tabel
print("Informasi Kendaraan di Parking Lot:")
table.create_table(len(parkinglot_content), len(parkinglot_header), parkinglot_content, parkinglot_header)


# Menyiapkan header dan konten tabel untuk daftar kendaraan
Vehicles_header = ["Plat Nomor", "Merk", "Tahun Produksi", "Warna", "Jenis Kendaraan"]
Vehicles_content = [[v.get_platNomor(), v.get_merk(), v.get_tahunProduksi(), v.get_warna(), "Car" if isinstance(v, Car) else "Motorcycle"] for v in vehicles]

# print daftar kendaraan dalam bentuk tabel
print("Daftar Kendaraan:")
table.create_table(len(Vehicles_content), len(Vehicles_header ), Vehicles_content, Vehicles_header )