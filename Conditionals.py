age = int(input("inform your age"))

if age >= 18:
    print("allowed")
else:
    print("not allowed")

salary = float(input("inform yopur salary"))

if salary <= 3000:
    print ("junior")
elif salary > 3000 and salary <= 6000:
    print ("Senior")
elif salary > 6000 and salary <= 15000:
    print ("pleno17")
else:
    print ("project manager")