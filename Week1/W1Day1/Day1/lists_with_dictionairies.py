
genies =[
    { "first":"Isaac",
        "last":"Newton",
        "domain":"physics",
        "age":52},
    {
        "first":"Albert",
        "last":"Einstein",
        "domain":"Energy",
        "age":81
    },
    {
        "first":"Max",
        "last":"Plank",
        "domain":"Chimestry",
        "age":47
    },
    {
        "first":"Nikolas",
        "last":"Tesla",
        "domain":"Electricity",
        "age":60
    },
    {
        "first":"Abderrahmen",
        "last":"Ibn Khaldoun",
        "domain":"Sociology",
        "age":130
    }
]
print(genies[0]["last"])
my_dictionary=genies[0]
print(my_dictionary["last"])
#Raed : Chimestry
print(f'chimestry {genies[2]["domain"]}')
print(f'Nickola {genies[3]["first"]}')
print(f'81 {genies[1]["age"]}')
print(f'sociolo {genies[-1]["domain"]}')

for i in range(len(genies)):
    print(f"the index is {i} and the value is {genies[i]} ")

for i in range(len(genies)):
    print(f"the index is {i} and the Last Name is {genies[i]['last']} ")
for i in range(len(genies)):
    print(f"the index is {i} and the First Name is {genies[i]['first']} ")
    
for i in range(len(genies)):
    if genies[i]["age"] <= 60:
        print(f"the index is {i} and the age is {genies[i]['age']} which is less or equal to 60 ")

for i in range(len(genies)):
     #print(genies[i])
    for key in genies[i]:
        print(f" the value is {genies[i][key]}")
    

