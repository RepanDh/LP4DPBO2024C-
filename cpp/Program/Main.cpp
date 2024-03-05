#include <bits/stdc++.h>
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "Garage.cpp"
#include "Parkinglot.cpp"

using namespace std;

int main(){


    // Membuat objek dari kelas Car dan Motorcycle
    Car car1(5, 4, "B 1234 CD", "Toyota", "2023", "Red");
    Motorcycle motor1("Sport", 10, "D 5678 EF", "Yamaha", "2024", "Blue");
    Car car2(4, 4, "E 9101 GH", "Honda", "2022", "White");
    Motorcycle motor2("Matic", 5, "F 1121 IJ", "Honda", "2023", "Black");

    // Membuat objek dari kelas Garage dan Parkinglot
    Garage garage1("Garasi 1", 100);
    Parkinglot parkinglot1(50);

    // Menambahkan kendaraan ke garasi
    garage1.addVehicle(car1);
    garage1.addVehicle(motor1);
    garage1.addVehicle(car2);
    garage1.addVehicle(motor2);

    // Menambahkan kendaraan ke parking lot
    parkinglot1.parkVehicle(car1);
    parkinglot1.parkVehicle(motor1);
    parkinglot1.parkVehicle(car2);
    parkinglot1.parkVehicle(motor2);

    // Menampilkan informasi kendaraan di garasi dalam bentuk tabel
    cout << "Informasi Kendaraan di " << garage1.GetNamaGarasi() << ":\n";
    cout << string(60, '-') << "\n";
    printf("|%-15s|%-15s|%-15s|%-10s|\n", "Plat Nomor", "Merk", "Tahun Produksi", "Warna");
    cout << string(60, '-') << "\n";
    for (Vehicle v : garage1.GetVehicles()) {
        printf("|%-15s|%-15s|%-15s|%-10s|\n", v.GetPlatNomor().c_str(), v.GetMerk().c_str(), v.GetTahunProduksi().c_str(), v.GetWarna().c_str());
    }
    cout << string(60, '-') << "\n";

    // Menampilkan informasi kendaraan di parking lot dalam bentuk tabel
    cout << "Informasi Kendaraan di Parking Lot:\n";
    cout << string(60, '-') << "\n";
    printf("|%-15s|%-15s|%-15s|%-10s|\n", "Plat Nomor", "Merk", "Tahun Produksi", "Warna");
    cout << string(60, '-') << "\n";
    for (Vehicle v : parkinglot1.GetVehicles()) {
        printf("|%-15s|%-15s|%-15s|%-10s|\n", v.GetPlatNomor().c_str(), v.GetMerk().c_str(), v.GetTahunProduksi().c_str(), v.GetWarna().c_str());
    }
    cout << string(60, '-') << "\n";

    return 0;
}
