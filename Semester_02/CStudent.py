from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
class student():
    def __init__(self,name, age, birth, id, irp, pps):
        self.name = name
        self.age = age
        self.birth = birth
        self.id = id
        self.irp = irp
        self.pps = pps

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nBirth: {self.birth}\nID: {self.id}\nIRP: {self.irp}\nPPS: {self.pps}\n"

name = input("Enter name: ")
age = int(input("Enter age: "))

birth = input("Enter birth date (DD/MM/YYYY): ")
while not is_valid_date(birth):
    print("Invalid date format or values. Please try again.")
    birth = input("Enter birth date (DD/MM/YYYY): ")

id = int(input("Enter ID: "))
irp = int(input("Enter IRP: "))
pps = int(input("Enter PPS: "))

print("-"*60, "\n")

students = student(name, age, birth, id, irp, pps)

print(students.get_details())