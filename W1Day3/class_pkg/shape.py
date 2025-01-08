#package=folder
#module=file

# my_int=10
# def say_hello():
#     print("Hello I'm in shape module")

# my_new_var=8
#from abc import abstractmethod,ABCMeta #abstract base class
from abc import ABC, abstractmethod
class Shape(ABC):
    #constructor
    def __init__(self,name,color):
        self.name=name
        self.color=color
    #instance method
    def print_info(self):
        print(f"The name of the shape is {self.name} and the color is {self.color}")
    
    #Polymorphism
    # def calculate_area(self):
    #     raise NotImplementedError
    #Abstraction
    @abstractmethod
    def calculate_area(self):
        pass
    