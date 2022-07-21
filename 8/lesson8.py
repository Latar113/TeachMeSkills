import time


class Auto:
    def __init__(self, brand, age, mark, color='black', weight=1700):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def birthday(self):
        self.age += 1
        return self.age

    def stop(self):
        print('stop')


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='red', weight=1700, ):
        self.max_load = max_load
        Auto.__init__(self, brand, age, mark, color='red', weight=1700)

    def move(self):
        print('attention move')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='black', weight=1700, ):
        self.max_speed = max_speed
        Auto.__init__(self, brand, age, mark, color='black', weight=1700)

    def move(self):
        print('attention move')
        print('max speed ' + str(self.max_speed))


audi_car = Auto(brand='Audi', age=2, color='white', mark='rs7', weight=1700)
lexus_car = Auto(brand='Lexus', age=7, color='black', mark='Ls', weight=2500)
track_maz = Truck(brand='MAZ', age=5, max_load=100000, mark='5743')
track_volvo = Truck(brand='Volvo', age=1, max_load=150000, mark='s905')
car_1 = Car(brand='mersedes', age=1, max_speed=230, mark='e200')
car_2 = Car(brand='mazda', age=9, max_speed=300, mark='rx7')

print(audi_car.color)
print(lexus_car.color)
print(car_2.color)
print(car_1.color)
print(track_volvo.color)
print(track_maz.color)