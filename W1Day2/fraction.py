class Fraction:
    #Class attribute
    description="This is a fraction class"
    list_of_fractions=[]
    
    #Constructor
    def __init__(self,fraction_name,numerator,denominator):
        #instance attributes
        self.fraction_name=fraction_name
        self.numerator=numerator
        self.denominator=denominator
        Fraction.list_of_fractions.append(self)
    #instance method    
    def print_info(self):
        print(f"the fraction {self.fraction_name} is {self.numerator}/{self.denominator}")
        #print(self.numerator/self.denominator)
        return self
    
    def divide_by_two(self):
        self.denominator=self.denominator*2
        
    def add_one_half_to_current_fraction(self):
        self.numerator=self.numerator*2+self.denominator
        self.denominator=self.denominator*2
    #instance method
    def add_one_half(self):
        new_numerator=self.numerator*2+self.denominator
        new_denominator=self.denominator*2
        new_fraction=Fraction("new_fraction",new_numerator,new_denominator)
        return new_fraction
    
    #instance method
    def add_fraction(self,another_fraction):
        resulting_numerator=self.numerator*another_fraction.denominator +another_fraction.numerator*self.denominator
        resulting_denominator=self.denominator*another_fraction.denominator
        new_fraction=Fraction("new_fraction",resulting_numerator,resulting_denominator)
        return new_fraction
    
    @classmethod
    def print_all_fractions(cls):
        for element in cls.list_of_fractions:
            element.print_info()
    
    @staticmethod
    def add_two_numberes(num1,num2):
        return num1+num2
    
    
fraction_one=Fraction("fraction_one",1,2)
fraction_two=Fraction("fraction_two",1,3)
#fraction_one.print_info()
#fraction_two.print_info()
#fraction_one.divide_by_two()
#fraction_one.print_info()
#fraction_two.add_one_half_to_current_fraction()
#fraction_two.print_info()
fraction_three=fraction_two.add_one_half()
#fraction_three.print_info()
fraction_four=fraction_two.add_fraction(fraction_two)
#fraction_four.print_info()
fraction_two.description="Hi I hacked the description of the class fraction"
# print(fraction_two.description)
# print(fraction_four.description)
# print(Fraction.description)
Fraction.description="I'm a super class, I can change the description for everyone"
# print(fraction_two.description)
# print(fraction_four.description)
# print(Fraction.description)
fraction_two.description=Fraction.description
#print(fraction_two.description)
Fraction.print_all_fractions()
print(Fraction.add_two_numberes(2,3))
