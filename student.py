# from numbers import Rational


class Student:
    name="Elizabeth"
    age=22
    school="Akirachix"
    nationality="Kenyan"
    
class Students:
    school="Akirachix"
    def __init__(self,name,age ,nationality):
        self.name=name
        self.age=age
        self.nationality=nationality
      
    def greet_student(self):
       return f"Hello {self.name}"
 
    def year_of_birth(self):
     year=2023-self.age
     return f"Hello{self.name}you were born in {year}"
 
#  1) Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials

class Student:
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def show_full_name(self):
            return f"{self.first_name} {self.last_name}"
    def year_of_birth(self):
            return f"{self.age}"
    def show_initials(self):
            return f"{self.first_name[0]} {self.last_name[0]}"
        
  
            