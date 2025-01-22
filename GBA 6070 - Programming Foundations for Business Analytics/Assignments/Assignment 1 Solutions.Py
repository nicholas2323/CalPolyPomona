A1_Petitt_Nicholas
GBA 6070 - Programming Fundamentals in Business Analytics
#Nicholas Petitt

1. Write Python statements which accept a person's first name, last name, and birth year,
respectively, and then display Hello followed by the full name; then in the next line, display the
person’s age. Write all your statements in one code cell. (5 points)
FYI, a sample output is as follows.
Enter a first name: John
Enter a last name: Smith
Enter a birth year: 2000
Hello John Smith
Your age is 25

import datetime

#Prompt the user to enter their first name
name = input("What is your first name?")

#Prompt the user to enter their last name
name = input("What is your last name?") 

#Calculate the year the user was born based on their age
current_year  = datetime.datetime.now(2025).year
birth_year = current_year - age

# Display a greeting message that includes the user's name and birth year
print(f"Hello {name}! You were born in {birth_year}."

2. Write statements to accept three numbers for length, width, and height of a cuboid,
respectively. Then display the surface area and volume; their displayed values will have
maximum two decimal numbers. Write all your statements in one code cell. (5 points)
FYI, a sample output is as follows, where xxx should be replaced by your calculated numbers.
Enter a length: 2.5
Enter a width: 2
Enter a height: 1.5
Surface area is xxx
Volume is xxx

length = float(input("Enter the length: 2.5 "))
width = float(input("Enter the width: 2 "))
height = float(input("Enter the height: 1.5"))

volume = length * width * height 
surface_area = 2 * (Length * width + width * height + height * length 

print(f"volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")

3. Write statements to collect a product unit price and quantity. When the quantity is greater
than or equals to 20, the discount rate is 0.05; quantity greater than or equals to 50, discount
rate is 0.1; quantity greater than or equals to 80, discount rate is 0.15. Display the total
discount and total amount (after discount), respectively, and their displayed values will have
maximum two decimal numbers. Write all your statements in one code cell. (5 points)
FYI, a sample output is as follows, where xxx should be replaced by your calculated numbers.
Enter a unit price: 12.5
Enter a quantity: 35
Total discount is $xxx
Total amount is $xxx

unit_priice = float(input("Enter the unit price: 12.5"))
quantity = int(input("Enter the quantity: 35"))

#Determine the discount rate based on the quantity 
if quantity >=80: 
   discount_rate = 0.15
   elif quantity >= 50: 
     discount_rate = 0.1
     elif quantity >= 20: 
       discount_rate = 0.05
     else: 
         discount_rate = 0
         
    # Calculate the total discount and total amount 
    total_discount = unit_price * quantity * discount_rate
    total_amount = unit_price * quantity - total_discount 
    
    #Display the results with two decimal pplaces
    print("Total discount: {:.2f}".format(total_discount))
    print("Total amount (after discount): {:.2f}".format(total_amount))
    
    
