
#Lists (python) are arrays (js)
students=["Alex","Martha","Ben","Julia"]
print(students[1])
students[2]="Ali"
print(students)
#pop(python) same as js
students.pop()
print(students)
#push (in js) becomes append in python
students.append("Mariem")
print(students)
#pop at any position
students.pop(2)
print(students)

#tuple : unmutable list
students_tuple=("Alex","Martha","Ben","Julia")
print(type(students_tuple))
#students_tuple.append("Ali")
print(students_tuple[1])
