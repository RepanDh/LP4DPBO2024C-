#pragma once
#include <iostream>
#include <string>
#include "Vehicle.cpp"
#include <vector>

using namespace std;

class Parkinglot
{
private:
    int kapasitas;
    int jumKendaraan;
    std::vector<Vehicle> vehicles;


public:
    Parkinglot(){

    }

    Parkinglot(int kapasitas){
        this->kapasitas = kapasitas;
        jumKendaraan = 0;
        this->vehicles = {};
    }
    Parkinglot(int kapasitas, int jumKendaraan){
        this->kapasitas = kapasitas;
        this->jumKendaraan = jumKendaraan;
        this->vehicles = {};
    }
    Parkinglot(int kapasitas, int jumKendaraan, std::vector<Vehicle> vehicles){
        this->kapasitas = kapasitas;
        this->jumKendaraan = jumKendaraan;
        vehicles = vehicles;
    }

    int GetKapasitas()  {
        return kapasitas;
    }

    void SetKapasitas(int kapasitas) {
        this->kapasitas = kapasitas;
    }

    int GetJumKendaraan()  {
        return jumKendaraan;
    }

    void SetJumKendaraan(int jumKendaraan) {
        this->jumKendaraan = jumKendaraan;
    }

    std::vector<Vehicle> GetVehicles()  {
        return vehicles;
    }

    void SetVehicles(std::vector<Vehicle> vehicles) {
        vehicles = vehicles;
    }

    void parkVehicle(Vehicle v) {
        if (jumKendaraan < kapasitas) {
            vehicles.push_back(v);
            jumKendaraan++;
        } else {
            std::cout << "Parking lot is full." << std::endl;
        }
    }

    ~Parkinglot(){

    }
};


