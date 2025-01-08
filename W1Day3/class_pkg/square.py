from class_pkg.shape import Shape
#inheritance concept
class Square(Shape):
    #constructor
    def __init__(self,name,color,side):
        super().__init__(name,color)
        self.side=side
        self.__identification=2 #private attribute
        
    #instance method (first way)
    def print_square_info(self):
        print(f"The name of the shape is {self.name} and the color is {self.color} and the side is {self.side}")
    
    #overriding
    def print_info(self):
        super().print_info()
        print(f"the side is {self.side}")
        
    #Polymorphism
    # def calculate_area(self):
    #     print( self.side*self.side)
    
    #Abstract not working
    def calculate_area(self):
        print( self.side*self.side)
    
    #Encapsulation
    def get_id(self):
        return self.__identification
    
    
    