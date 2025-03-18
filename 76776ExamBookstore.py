totalcart = 0.
booksprice = 7.5
books = 0
conditional = True
more = True
discounts = 0.0
finalvalue = 0.0

while totalcart >= 0 :
      
    if conditional == True:
        books = books + int(input("How many books do you want: "))
        booksprice = float(input("How much is each book? "))
        totalcart = books * booksprice 
        print("total is " , totalcart)
        conditional = input("Would you like to add any book else? Y/N ").lower().strip() == 'y'
    else:
        if books >= 3:
          discounts = 0.15 * totalcart 
          finalvalue = totalcart - discounts - 5.0
          print("The total is:",books, "books for ",totalcart,", You have earned: 15% bulk discount and €5 promotion discount. So the final value is:",finalvalue)
          more = input("Would you like to add any book else? Y/N ").lower().strip() == 'y'
          if more == True:
                conditional = True
                print("OK, add more books \n")
          else:
             print("Thank you for the purchased")
             break

        else:
          discounts = 0.15 * totalcart 
          finalvalue = totalcart - discounts
          print("The total is:",books, "books for ",totalcart,", You have earned: 15% bulk discount: So the final value is: ",finalvalue)
          more = input("Would you like to add any book else? Y/N ")
          if more == True:
                conditional = True
                print("OK, so add more books \n")
          else:
             print("Thank you for the purchased")
             break