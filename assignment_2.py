class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car is driving."
    
class Plane(Vehicle):
    def move(self):
        return "The plane is flying."
    
class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedaling."

# Example of using the classes
vehicles = [Car(), Plane(), Bicycle()]
for vehicle in vehicles:
    print(vehicle.move())