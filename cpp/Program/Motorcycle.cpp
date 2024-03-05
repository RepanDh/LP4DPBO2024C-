#pragma once
#include <iostream>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Motorcycle : public Vehicle
{
private:
    string jenisMotor;
    int kapasitasTangki;


public:
    Motorcycle(){

    }

    Motorcycle(string jenisMotor, string platNomor, string merk, string tahunProduksi, string warna) : Vehicle(platNomor, merk, tahunProduksi, warna){
        this->jenisMotor = jenisMotor;
        kapasitasTangki = 0;
    }

    Motorcycle(string jenisMotor, int kapasitasTangki, string platNomor, string merk, string tahunProduksi, string warna) : Vehicle(platNomor, merk, tahunProduksi, warna){
        this->jenisMotor = jenisMotor;
        this->kapasitasTangki = kapasitasTangki;
    }

    string GetJenisMotor()  {
        return jenisMotor;
    }

    void SetJenisMotor(string jenisMotor) {
        this->jenisMotor = jenisMotor;
    }

    int GetKapasitasTangki()  {
        return kapasitasTangki;
    }

    void SetKapasitasTangki(int kapasitasTangki) {
        this->kapasitasTangki = kapasitasTangki;
    }

    ~Motorcycle(){

    }
};

