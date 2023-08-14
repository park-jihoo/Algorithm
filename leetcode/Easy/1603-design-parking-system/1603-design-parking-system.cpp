#include <vector>
class ParkingSystem {
public:
  vector<int> slot = {0, 0, 0};
  ParkingSystem(int big, int medium, int small) {
    this->slot = {big, medium, small};
  }

  bool addCar(int carType) {
    if (this->slot[carType - 1] == 0)
      return false;
    else {
      this->slot[carType - 1] -= 1;
      return true;
    }
  }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */