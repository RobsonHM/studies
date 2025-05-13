from datetime import datetime
import math

allstudents = []

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False
       
class student():
    def __init__(self,name, age, birth, id, email, phone):
        self.name = name
        self.age = age
        self.birth = birth
        self.id = id
        self.email = email
        self.phone = phone

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nBirth: {self.birth}\nID: {self.id}\nEmail: {self.email}\nPhone: {self.phone}"
    
while True:
    name = input("Enter name: ")
    birth = input("Enter birth date (DD/MM/YYYY): ")
    while not is_valid_date(birth):
        print("Invalid date format or values. Please try again.")
        birth = input("Enter birth date (DD/MM/YYYY): ")

    today = datetime.now()
    yearbith = datetime.strptime(birth, "%d/%m/%Y")
    age = (today - yearbith).days
    age = math.floor((age/365.25))

    id = int(input("Enter ID: "))
    email = input("Enter the email: ")
    phone = int(input("Enter the phone: "))
    print("-"*60, "\n")
    students = student(name, age, birth, id, email, phone)
    allstudents.append(students)
    anyelse = input("would you like to add anyone else? Y/N: ")
    if anyelse.lower() != "y":
        print("-"*60)
        break

AnyStudent = input("Would you like to choose a student? Y/N: ")

if AnyStudent.lower() == "y":
    student_id = int(input("Enter their ID: "))

    found = False
    for student in allstudents:
        if student.id == student_id:
            print("\nStudent found:")
            print(student.get_details())
            found = True
            break

    if not found:
        print("No student found with that ID.")
else:
    print("\nAll students:\n")
    for student in allstudents:
        print(student.get_details())
