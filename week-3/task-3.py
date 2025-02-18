class Vehicle:
    def __init__(self, make, model):
        self.make = make  
        self._model = model   # Encapsulation : making it protected but in python it is acccesible without getter and setter

    


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors  # Encapsulation : making it private

    def get_num_doors(self):  # getter for private attribute
        return self.__num_doors



    def describe(self):  # Polymorphism
        return f"{self._model} has {self.__num_doors} doors."


class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def describe(self):  # polymorphism the same function as the above one but different return value
        return f"{self._model} is a racing bike."


car1 = Car('Toyota', 'Corolla', 4)
print('Manufacturer : ', car1.make)
print('Model : ', car1._model)
print(car1.describe())
bike1 = Bike('Yamaha', 'YZF-R1')
print('Manufacturer : ', bike1.make)
print('Model : ', bike1._model)
print(bike1.make, bike1.describe())
