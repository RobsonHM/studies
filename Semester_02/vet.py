class animals:
    def __init__(self, owner, name, age, colour, weight, symptom):
        self.owner = owner
        self.name = name
        self.age = age
        self.colour = colour
        self.weight = weight
        self.symptom = symptom

    def get_datails(self):
     return f"{self.name} showed these symtoms:\n{self.symptom}"

owner = input("Enter the owner's name: ")
name = input("Enter the animal's name: ")
age = int(input("Enter the animal's age: "))
colour = input("Enter the animal's colour: ")
weight = float(input("Enter the animal's weight: "))
symptom = input("What is its symptom?\n")

print("-"*60 ,"\n")

animal = animals(owner,name,age,colour,weight,symptom)

print(animal.get_datails())