#in js function myFunction(param...){}
x=11
y=7
def my_function(a,b):
    #pass
    total=a+b
    return total

my_total=my_function(7,5)
print(my_total)

my_total=my_function(x,y)
print(my_total)

#default parameters
def multiply_two_numbers(b=2,a=1):
    total=a*b
    return total
#no default parameters
new_total=multiply_two_numbers(4,5)#4*5=20
print(new_total)
#1 default parameters
new_total=multiply_two_numbers(5)#1 (a) *5=5
print(new_total)
#2 default parameters
new_total=multiply_two_numbers()#1 (a) *2 (b)=2
print(new_total)

