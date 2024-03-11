# LP4DPBO2024C-

## janji

Saya Repan Dhia Nararya NIM [2202331] mengerjakan Latihan Praktikum Desain Pemrograman Berorientasi Objek dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

### Deskripsi Program
Program berbasis Object Oriented yang ditulis dalam bahasa pemrograman C++ dan Python. Program ini mengimplementasikan konsep Inheritance, Composite dan Encapsulation melalui berbagai class, yaitu Vehicle, Car, Motorcycle, Garage, ParkingLot, dan Table.
  
Pada Main.py, beberapa objek Car dan Motorcycle dibuat dan ditambahkan ke objek Garage dan ParkingLot. Kemudian, informasi tentang kendaraan di Garage dan ParkingLot ditampilkan dalam bentuk tabel.

### Penjelasan Desain Program
Program didesain menjadi 6 class, yaitu Vehicle, Car, Motorcycle, Garage, ParkingLot, dan Table. Class Vehicle merupakan class induk dari class Car dan Motorcycle.

- Vehicle: Class yang mendefinisikan atribut dan metode umum untuk kendaraan, seperti platNomor, merk, tahunProduksi, dan warna.
- Car dan Motorcycle: Kedua Class ini mewarisi dari kelas Vehicle dan menambahkan atribut khusus mereka sendiri. Car memiliki atribut jumKursi dan jumPintu, sementara Motorcycle memiliki jenisMotor dan kapasitasTangki.
- Garage dan ParkingLot: Kedua Class ini berfungsi sebagai wadah untuk objek Vehicle, yang mana kedua Class ini memiliki metode untuk menambahkan kendaraan. Di dalam kedua class ini terdapat implementasi Composite, dimana kedua class ini terdiri dari objek-objek Vehicle
- Table: Kelas ini digunakan untuk mencetak informasi tentang kendaraan dalam format tabel.

### Desain Relasi
![p3 drawio](https://github.com/RepanDh/LP4DPBO2024C-/assets/133224998/7f2e7f52-5967-4a78-8fa4-50ace1152ddd)

class Vehicle ini memiliki atribut:
-platNomor: Nomor plat kendaraan.
-merk: Merk atau produsen kendaraan.
-tahunProduksi: Tahun produksi kendaraan.
-warna: Warna kendaraan.

class Car Sebagai turunan dari Vehicle, kelas ini memiliki semua atribut Vehicle ditambah dengan:
-jumKursi: Jumlah kursi di mobil.
-jumPintu: Jumlah pintu di mobil.

class Motorcycle Sebagai turunan dari Vehicle, kelas ini memiliki semua atribut Vehicle ditambah dengan:
-jenisMotor: Jenis motor.
-kapasitasTangki: Kapasitas tangki bensin motor.

class Garage ini memiliki atribut:
-namaGarasi: Nama garasi.
-luasGarasi: Luas garasi.
-kendaraan: Daftar kendaraan yang disimpan di garasi.

class ParkingLot ini memiliki atribut:
-kapasitas: Kapasitas maksimum parking lot.
-jumKendaraan: Jumlah kendaraan saat ini di parking lot.
-kendaraan: Daftar kendaraan yang disimpan di parking lot.

class Tabel memiliki atribut :
- baris
- kolom

### Dokumentasi program

![Screenshot 2024-03-11 075247](https://github.com/RepanDh/LP4DPBO2024C-/assets/133224998/7178b8da-f536-4d30-8aad-48dcb7d4639b)
![Screenshot 2024-03-11 075243](https://github.com/RepanDh/LP4DPBO2024C-/assets/133224998/f54da653-5a12-4672-bd32-43380c301076)
