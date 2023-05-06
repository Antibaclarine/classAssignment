# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them

# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.
class Car:
    wheels=4
    def __init__(self,make,model,year,speed,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.speed=speed
    def age_of_car(self):
        return f"the car is {2023-self.year} years"
    def car_details(self):
        return f"This is car is a{self.make} {self.model} {self.color}"
    def distance_between(self,time):
        self.time=time
        return f"the car covered a distance of {self.speed *time} km/hr"
    
        
        