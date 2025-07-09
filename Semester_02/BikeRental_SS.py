
import datetime as dt
import time as t
from tabulate import tabulate as tb
import re
import math

all_bikes = []
print(dt.datetime.now())

#print(tb([[1, 2], [3, 4]], headers=["A", "B"]))


class bikes:

   def __init__(self, bike_id, model, type, available, price):
        self.bike_id = bike_id
        self.model = model
        self.type = type
        self.available = available
        self.price = price
   
   def get_row(self):
        return [self.bike_id, self.model, self.type, self.available,  f"€{self.price:.2f}"]

   def get_details(self):
      data = [[self.bike_id, self.model, self.type, self.available]]
      headers = ["ID", "Model", "Type", "Available"]
      return tb(data, headers=headers, tablefmt="grid")

   #    return f"\nBike ID: {self.bike_id}\nBike model: {self.model}\nType: {self.type}\nAvailable: {self.available}\n"+("-"*40)


class rental:

   def __init__(self, customer_name, bike_id, start_time, end_time=None):
        self.customer_name = customer_name
        self.bike_id = bike_id
        self.start_time = start_time
        self.end_time = end_time


   def get_details(self):
       return f"Customer: {self.customer_name}\nBike ID: {self.bike_id}\nStart time: {self.start_time}\nEnd Time: {self.end_time}"

def is_valid_name(name_srt):
    return bool(re.match(r'[a-zA-Z ]{2,50}$',name_srt))

def is_valid_id(id_srt):
    return bool (re.match(r'[0-9]{1,5}', id_srt))

def is_valid_model(model):
    return bool(re.match(r"[A-Za-z0-9\- ]{2,30}", model))

def is_valid_type(type_srt):
    return bool(re.match(r'[a-zA-Z0-9\- ]', type_srt))

def is_valid_rent(rent_srt):
    return bool(rent_srt)

def is_available(available_srt):
    return available_srt in ["yes", "no"]

def rent_days(days_srt):
   start_time = dt.datetime.now()
   end_time = start_time + dt.timedelta(days=days_srt)
   print ("\033[31mYou have to return it on\033[0m",end_time.strftime("%Y-%m-%d %H:%M"))
   return start_time, end_time



all_bikes = [
    bikes(1, "CityRide 300",   "Urban",    True,3),
    bikes(2, "EcoSprint X",    "Electric", False,2),
    bikes(3, "MTB Storm 500",  "Mountain", True,1),
    bikes(4, "UrbanLite",      "Urban",    True,4),
    bikes(5, "TrailBlazer 4",  "Mountain", False,3),
    bikes(6, "VoltCity Pro",   "Electric", True,2),
    bikes(7, "Speedster 700",  "Road",     True,1),
    bikes(8, "CargoMax Duo",   "Cargo",    False,2),
    bikes(9, "FlexFold Mini",  "Folding",  True,4),
    bikes(10, "Gravel X One",   "Gravel",   True,5)
]

all_bikes_rent = [
    rental("Alice", 1, dt.datetime(2025, 7, 1, 9, 0), dt.datetime(2025, 7, 29, 9, 0)),
    rental("Bob", 2, dt.datetime(2025, 7, 2, 10, 30), dt.datetime(2025, 7, 6, 10, 30)),
    rental("Carla", 3, dt.datetime(2025, 7, 3, 14, 15), dt.datetime(2025, 7, 8, 14, 15)),
    rental("Diego", 4, dt.datetime(2025, 7, 4, 8, 45), dt.datetime(2025, 7, 10, 8, 45)),
    rental("Eva", 5, dt.datetime(2025, 7, 5, 13, 0), dt.datetime(2025, 7, 12, 13, 0)),
    rental("Felipe", 6, dt.datetime(2025, 7, 6, 9, 30), dt.datetime(2025, 7, 15, 9, 30)),
    rental("Giovana", 7, dt.datetime(2025, 7, 7, 11, 0), dt.datetime(2025, 7, 14, 11, 0)),
    rental("Hugo", 8, dt.datetime(2025, 7, 8, 16, 20), dt.datetime(2025, 7, 13, 16, 20)),
    rental("Isabela", 9, dt.datetime(2025, 7, 9, 10, 0), dt.datetime(2025, 7, 16, 10, 0)),
    rental("João", 10, dt.datetime(2025, 7, 10, 15, 30), dt.datetime(2025, 7, 17, 15, 30)),
]

while True:

   option = int(input("choose an option:\n1 Display all available bikes\n2 add new bike\n3 Rent a bike\n4 return a bike\n5 search bikes by type or ID\n6 Exit and save data "))
   #display all bike
   if option == 1:
      bike_rows = [bikes.get_row() for bikes in all_bikes]
      headers = ["ID", "Model", "Type", "Available", "Daily Price"]
      print(tb(bike_rows, headers=headers, tablefmt="grid"))
      print("\n")
      t.sleep(2)

   elif option == 2:
         
         while True:
            existent_ids = {bike.bike_id for bike in all_bikes}
            last_id = sorted(existent_ids)[-1]
            last_id = last_id + 1
            print(last_id)

            bike_models = input("what is the type? ")
            while not is_valid_model(bike_models):
               print("erro type")
               bike_models = input("what is the model? ")

            bikes_type = input("type? ")
            while not is_valid_type(bikes_type):
               print("it's still wrong ")
               bikes_type = input("type? ")

            bike_avai = input("Is it already available now? Yes or No ").strip().lower()
            while not is_available(bike_avai):
                bike_avai = input("Is it already available now? Yes or No ").strip().lower()
            
            bike_ids = last_id
            bike = bikes(bike_ids, bike_models, bikes_type, bike_avai, 4)
            all_bikes.append(bike)
            add_more = input("add more? Y/N").strip().lower()
            if add_more != 'y':
               break



   elif option == 3:
      customer_name = input("enter your name: ")
      while not is_valid_name(customer_name): 
         customer_name = input("enter your name: ")

      see_list = input("see the list? ")
      if see_list == "y":
         bike_rows = [bikes.get_row() for bikes in all_bikes]
         headers = ["ID", "Model", "Type", "Available"]
         print(tb(bike_rows, headers=headers, tablefmt="grid"))
         print("\n")
         t.sleep(2)

      bike_rent = int(input("What bike would you like to rent?: type ID "))

      while True:
         for bikes in all_bikes:
            if bikes.bike_id == bike_rent:
               print(bikes.get_details())
               teste = input("find other one? ")
               if teste == "y":
                   bike_rent = int(input("What bike would you like to rent?: "))
         break
          
      rent_time = int(input("How many days would you like to rent it?: "))
      rent_days(rent_time)
      change_day = input("Would you like to change the day? Yes/No").strip().lower()
      while change_day not in ["no", "n"]:
            rent_time = int(input("How many days would you like to rent it?: "))
            rent_days(rent_time)
            change_day = input("Would you like to change the day? Yes/No").strip().lower()
      start_time, end_time = rent_days(rent_time)

      existent_ids = {bike.bike_id for bike in all_bikes}
      last_id = sorted(existent_ids)[-1]
      last_id = last_id + 1

      rent = rental(customer_name, last_id, start_time, end_time)

      print(start_time,end_time)

      print("\033-\033[0m")
      print("\033[32mTexto em verde\033[0m")
      print("\033[33mTexto em amarelo\033[0m")
      print("\033[34mTexto em azul\033[0m")

   elif option == 4:


      bikeid = int(input("Type the ID of the bike you want to return: "))
      for bikes in all_bikes:
          if bikes.bike_id == bikeid:
            print(bikes.get_details())
            price = bikes.price 

      # to fazendo essa parte do calculo dos dias 
      for rental in all_bikes_rent:
            if rental.bike_id == bikeid:
               end_time = rental.end_time
               start_time = rental.start_time 
               total = (dt.datetime.now() - end_time).days
               days_rented = (dt.datetime.now() - start_time).days
               #print(total, days_rented)
               if total < 0:
                   pay = math.floor((dt.datetime.now() - start_time).days * price)
                   print(f"You are late, you have to pay more 10% per day delayied, total is {pay * price} ")
               print(f"\nyou return the bike {-total} days ealier ")
               print(f"you have to pay: {price * days_rented}€\n")
      
      return_it = input("\033[31mwould you like to return this bike? YES/NO \033[0m \n")

   elif option == 5:
      bike_id = 1
      for bikes in all_bikes_rent:
         if bikes.bike_id == bike_id:
            print(bikes)
            print("search bike by id or type")

   else:
      print("saved")
      break
    

"""bike_available = bike_rented

bike_st = ""

bike_et = ''"""
