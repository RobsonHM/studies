tblood  = {
    "A+": {"gives": ["A+", "AB+"], "receives": ["A+", "A-", "O+", "O-"]},
    "O+": {"gives": ["O+", "A+", "B+", "AB+"], "receives": ["O+", "O-"]},
    "B+": {"gives": ["B+", "AB+"], "receives": ["B+", "B-", "O+", "O-"]},
    "AB+": {"gives": ["AB+"], "receives": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]},
    "A-": {"gives": ["A+", "A-", "AB+", "AB-"], "receives": ["A-", "O-"]},
    "O-": {"gives": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], "receives": ["O-"]},
    "B-": {"gives": ["B+", "B-", "AB+", "AB-"], "receives": ["B-", "O-"]},
    "AB-": {"gives": ["AB+", "AB-"], "receives": ["AB-", "A-", "B-", "O-"]},
}

print("Welcome to the Blood Type Compatibility Checker!")
print("Choose an option: \n 1. Check who can donate to your blood type. \n 2. Check who you can donate blood to. \n 3. Exit the program.\n")

continues = True

while continues:
    try:
        option = int(input("Enter your choice (1/2/3): "))
        if option == 1:
            Myblood = input("Enter your blood type (e.g., A+, O-, AB+): ").strip().upper()
            if Myblood in tblood:
                print(f"Blood Type {Myblood} can receive donations from: {tblood[Myblood]['receives']}")
            else:
                print(f"Invalid blood type: {Myblood}. Please try again.")
        elif option == 2:
            Myblood = input("Enter your blood type (e.g., A+, O-, AB-): ").strip().upper()
            if Myblood in tblood:
                print(f"Blood Type {Myblood} can donate to: {tblood[Myblood]['gives']}")
            else:
                print(f"Invalid blood type: {Myblood}. Please try again.")
        elif option == 3:
            print("Thank you for using the Blood Type Compatibility Checker. Goodbye!")
            continues = False
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid number (1, 2, or 3).")
