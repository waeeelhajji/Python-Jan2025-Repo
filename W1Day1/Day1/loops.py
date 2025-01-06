for i in range(10): # js : for (let i=0;i<10;i++)
    print(i)
print("*"*10)
for i in range(5,10):#js for (let i=5;i<10,i++)
    print(i)
print("*"*10)
for i in range(20,10,-1): #js for (let i=20; i>10;i--)
    print(i)

for i in range(20,10,-2): #js for (let i=20; i>10;i-=2)
    print(i)

#Loop through lists
#in js for(let i=0;i<araay.length;i++){}
students=["Ala", "Mariem", "Anouar", "Ghada"]
print(len(students))
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print("*"*10)
for i in range(len(students)):#in js for(let i=0;i<students.length;i++){}
    print(students[i])
print("*"*10)
for element in students:
    print(element)
    
number_array=[2,3,4,5]
for element in number_array:
    print(element)
    
print("*"*10)
for i in range(len(students)-1,0,-1) :#in js for (let i=students.length-1,i>=0,i--)
    print(students[i])

student_info={
    "first_name":"Ala",
    "last_name":"Abidi",
    "age":22
}
print("*"*10)
for value in student_info:
    #print(key)
    print(f"the key is {value} and the  value is ")

a=10
while a>0:
    print(a)
    a=a-1
    a-=1
    #a-- a++ don't exist in python






    
