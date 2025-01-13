#dictionaries are objects in js.
#Key_value pair
student={
    "first_name":"Alex",
    "last_name":"Miller",
    "age":32
}
print(type(student))
student["age"]=20
print(f"my first name is {student['first_name']} my last name is {student['last_name']} \nand my age is {student['age']}")
student.pop("last_name")
print(student)
student["last_name"]="Allan"
print(student)
student["grade"]=8.5

print(student)

