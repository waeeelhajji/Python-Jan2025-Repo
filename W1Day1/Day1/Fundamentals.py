
# This is a comment
#Data types: primitive datatypes in JS: Boolean, Number, String, undefined, Null
#Primitive Datatypes in Python: String, int (integer), float, complex (j), Boolean, None 
#Strings
first_name="Alex" #string
wf_grade=8.5 #float
age=22 #integer
complex_number=4+2j#complex
marriage_status=False#boolean
happy=True #boolean
#printing: in JS console.log
#in python: print
print(type(first_name))
print(wf_grade)
print(age)
print(type(complex_number))
print(happy)
#None
java_grade=None
print(type(java_grade))
print(first_name+str(age))
#print(int(complex_number)) #Casting only when possible
print(first_name.upper())
import random
print(random.randint(2,52))
#formatting strings
#f-strings: Recommanded
print(f'My first name is {first_name} and my age is {age}')
#% formatting
print("My first name is %s and my age is %d"%(first_name,age))
#string.format()
print("My first name is {0} and my age is {1}".format(first_name,age))
