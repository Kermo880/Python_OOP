class Car:
    def __init__(self,make,model,year,mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

    def drive(self, distance):
        self.mileage = self.mileage + distance

car = Car("Honda","Civic","2001",100000)

car.drive(200)
print(car.get_mileage())