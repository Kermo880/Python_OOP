class Car:
    def __init__(self, speed, max_speed):
        self.__speed = speed
        self.__max_speed = max_speed
        
    def get_speed(self):
        return self.__speed
    
    def get_max_speed(self):
        return self.__max_speed
    
    def kiirenda(self, speed):
        new_speed = self.__speed + speed
        if new_speed > self.__max_speed:
            self.__speed = self.__max_speed
        else:
            self.__speed = new_speed

    def stop(self):
        self.__speed = 0

class Supercar(Car):
    def __init__(self, max_speed):
        super().__init__(0, max_speed)
        self.__turbo = False
        
    def get_turbo(self):
        return self.__turbo
    
    def activate_turbo(self):
        if not self.__turbo:
            if self.get_max_speed() == 2*self._Car__max_speed:
                print("Cannot activate turbo. Maximum speed already doubled.")
            else:
                self.__turbo = True
                self._Car__max_speed *= 2
                print("Turbo activated. Maximum speed now:", self.get_max_speed())
        else:
            print("Turbo already activated. Maximum speed:", self.get_max_speed())


    
    def use_turbo(self):
        self.activate_turbo()

if __name__ == '__main__':
    speed = 0
    max_speed = 200
    my_car = Car(speed, max_speed)
    my_car.kiirenda(50)
    print(my_car.get_speed())

    my_car.kiirenda(200)
    print(my_car.get_speed())

    my_car.stop()
    print(my_car.get_speed())

    my_supercar = Supercar(max_speed)

    my_supercar.activate_turbo()

    my_supercar.activate_turbo()