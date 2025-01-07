#define the class = template
class Table:
    #methods are functions that exist in a class
    #Constructor
    def __init__(self,material,width,hight,shape,manufacturer,owner,color):
        self.material=material#caracteristics are Instance attributes
        self.width=width #Instance attributes
        self.hight=hight #Instance attributes
        self.shape=shape #Instance attributes
        self.manufacturer=manufacturer #Instance attributes
        self.owner=owner #Instance attributes
        self.color=color # Instance attributes
    #method are actions inside the class Table
    def print_caracteristics(self):
        print(self.owner)
        print(self.shape)
        print(f"Hi this table belongs to {self.owner} it has a shape of {self.shape} ")
    #Instance method
    def study(self):
        print(f"{self.owner} is studying on the table")
    
    def calculate_area(self):
        return self.hight*self.width
        
#give life to the class: create an instance of the class = object
ahmed_table=Table("wood",120,100,"rectangular","Ikea","ahmed","Brown")
sarra_table=Table("iron",45,150,"circular","mublatex","sarra","white")
oliver_table=Table("plastic",78,400,"triangle","Sassi Bois","Oliver","Black")
print(ahmed_table.owner)
print(ahmed_table.manufacturer)
print(ahmed_table)
ahmed_table.print_caracteristics()
sarra_table.print_caracteristics()
print(sarra_table.owner)
oliver_table.study()
print(ahmed_table.color)
ahmed_table.color="red"
print(ahmed_table.color)

area=oliver_table.calculate_area()
print(area)

