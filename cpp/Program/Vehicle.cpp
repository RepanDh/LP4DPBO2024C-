#pragma once
#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
private:
    string platNomor;
    string merk;
    string tahunProduksi;
    string warna;

public:

    Vehicle(){

    }

    Vehicle(string platNomor){
        this->platNomor = platNomor;
        merk = "";
        tahunProduksi = "";
        warna = "";
    }

    Vehicle(string platNomor, string merk){
        this->platNomor = platNomor;
        this->merk = merk;
        tahunProduksi = "";
        warna = "";
    }

    Vehicle(string platNomor, string merk, string tahunProduksi){
        this->platNomor = platNomor;
        this->merk = merk;
        this->tahunProduksi = tahunProduksi;
        warna = "";
    }

    Vehicle(string platNomor, string merk, string tahunProduksi, string warna){
        this->platNomor = platNomor;
        this->merk = merk;
        this->tahunProduksi = tahunProduksi;
        this->warna = warna;
    }

    string GetPlatNomor() {
    return platNomor;
    }

    void SetPlatNomor(string platNomor) {
    this->platNomor = platNomor;
    }

    string GetMerk() {
        return merk;
    }

    void SetMerk(string merk) {
        this->merk = merk;
    }

    string GetTahunProduksi() {
        return tahunProduksi;
    }

    void SetTahunProduksi(string tahunProduksi) {
        this->tahunProduksi = tahunProduksi;
    }

    string GetWarna() {
        return warna;
    }

    void SetWarna(string warna) {
        this->warna = warna;
    }

     ~Vehicle()
    {


    }

    
};

