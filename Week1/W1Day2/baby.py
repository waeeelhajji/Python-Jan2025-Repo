class Baby:
    def __init__(self,baby_name,mother_name,gender,age):
        self.baby_name=baby_name
        self.mother_name=mother_name
        self.gender=gender
        self.age=age
        self.energy=10
    
    def print_info(self):
        print(f"Hi my name is {self.baby_name} , my mother name is {self.mother_name},  \nand I'm {self.age} months old and I'm a {self.gender}")

    def play(self):
        if self.energy<=4:
            print("I'm tired, I need to take a nap")
        else:
            self.energy=self.energy-5
            self.age+=1
        return self
            
    def sleep(self):
        self.energy=10
        print("I'm ready to play again")
        return self
    def print_age(self):
        print(self.age)
        return self
        
    
Oussama=Baby("Oussama","Fedia","Boy",7)
Asma=Baby("Asma","Sarra","girl",10)
Oussama.print_info()
Asma.print_info()
Asma.play()
print(Asma.energy)
Asma.play()
print(Asma.energy)
Asma.play()
Asma.sleep()
print(Asma.energy)
#chaining mecanism
Asma.play().play().play().sleep().play().print_age()