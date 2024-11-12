'''
Vehicle Hierarcy challenge
'''
class Vehicle:
    
    def __init__(self, manufacturer: str, model: str, year: int):
        self.manufacturer = manufacturer
        self.model= model
        self.year= year
    def get_details(self):
        print(f"The vehicle is {self.model} and is manufactured by {self.manufacturer} on {self.year} year")
    

class Car(Vehicle):
    
    def __init__(self, manufacturer: str, model: str, year: int, num_doors: int):
        super().__init__(manufacturer, model, year)
        self.num_doors= num_doors
    def get_details(self):
        print(f"The vehicle is {self.model}and is manufactured by {self.manufacturer} on {self.year} year and it has {self.num_doors} doors")

class Motorcycle(Vehicle):
    
    def __init__(self, manufacturer: str, model: str, year: int, top_speed:float):
        super().__init__(manufacturer, model, year)
        self.top_speed= top_speed
    def get_details(self):
        print(f"The vehicle is {self.model}and is manufactured by {self.manufacturer} on {self.year} year that has a speed of {self.top_speed}")

class Truck(Car):
    def __init__(self, manufacturer: str, model: str, year: int, num_doors: int, cargo_capacity:float):
        super().__init__(manufacturer, model, year, num_doors)
        self.cargo_capcity= cargo_capacity
    def get_details(self):
        print(f"The vehicle is {self.model}and is manufactured by {self.manufacturer} on {self.year} year and it has {self.num_doors} doors with a cargo capacity of {self.cargo_capcity}")

toyota= Vehicle ("Toyota", "Camry", 2023)
toyota.get_details()

ferrari= Car("ferrari","ferrari 488 GTB", 2021, 2)
ferrari.get_details()

ducati= Motorcycle("Ducati","Panigale V4", 2023, 186.4)
ducati.get_details()

ford= Truck("Ford", "F-150", 2022, 4, 3_325)
ford.get_details()

