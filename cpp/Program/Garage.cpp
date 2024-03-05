#pragma once
#include <iostream>
#include <string>
#include "Vehicle.cpp"
#include <vector>

using namespace std;

class Garage
{
private:
    string namaGarasi;
    int luasGarasi;
    std::vector<Vehicle> vehicles;

public:
    Garage(){

    }

    Garage(string namaGarasi){
        this->namaGarasi = namaGarasi;
        luasGarasi = 0;
        this->vehicles = {};
    }

    Garage(string namaGarasi, int luasGarasi){
        this->namaGarasi = namaGarasi;
        this->luasGarasi = luasGarasi;
        this->vehicles = {};
    }

    Garage(string namaGarasi, int luasGarasi, std::vector<Vehicle> vehicles){
        this->namaGarasi = namaGarasi;
        this->luasGarasi = luasGarasi;
        vehicles = vehicles;
    }


    string GetNamaGarasi()  {
        return namaGarasi;
    }

    void SetNamaGarasi(string namaGarasi) {
        this->namaGarasi = namaGarasi;
    }

    int GetLuasGarasi()  {
        return luasGarasi;
    }

    void SetLuasGarasi(int luasGarasi) {
        this->luasGarasi = luasGarasi;
    }

    std::vector<Vehicle> GetVehicles()  {
        return vehicles;
    }

    void SetVehicles(std::vector<Vehicle> vehicles) {
        vehicles = vehicles;
    }

    void addVehicle(Vehicle v) {
        vehicles.push_back(v);
    }

    ~Garage(){

    }
};

