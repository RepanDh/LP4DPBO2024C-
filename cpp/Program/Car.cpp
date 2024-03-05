#pragma once
#include <iostream>
#include <string>
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle
{
private:
    int jumKursi;
    int jumPintu;
    

public:
    Car(){

    }

    Car(int jumKursi, string platNomor, string merk, string tahunProduksi, string warna) : Vehicle(platNomor, merk, tahunProduksi, warna){
        this->jumKursi = jumKursi;
        jumPintu = 0;
    }

    Car(int jumKursi, int jumPintu, string platNomor, string merk, string tahunProduksi, string warna) : Vehicle(platNomor, merk, tahunProduksi, warna){
        this->jumKursi = jumKursi;
        this->jumPintu = jumPintu;
    }

    int GetJumKursi()  {
        return jumKursi;
    }

    void SetJumKursi(int jumKursi) {
        this->jumKursi = jumKursi;
    }

    int GetJumPintu()  {
        return jumPintu;
    }

    void SetJumPintu(int jumPintu) {
        this->jumPintu = jumPintu;
    }

    ~Car(){

    }
};

