Write a Boolean Expression according to each of the following requirements

 [1] Whether age is between 18 and 55
age = 35
is_in_range = 18 <= age <= 55 
print (is_in_range)
    
 [2] Whether grade is at least 3.0 and program is 'MSBA'
 
 grade = float(input("Enter your grade: "))
 program = input("Enter your program: ")
 
 if grade >= 3.0 and pr ogram == "MSBA":
     print("You are eligible for graduation.")
 else: 
     print("You are not eligible for graduation." 
 
 [3] Whether program is 'MSBA', 'MSIS', or 'MSDM'
if program is 'MSBA' or 'MSIS' or 'MSDM'
 then: 
     # Print 'MSBA' or 'MSIS' or 'MSDM'
  
 [4] Whether program is not 'MBA' and age is between 22 and 30
 
def check_age_and_program(age, program): 
    """Checks if age is within a range and program is not a specific value."""
    
    is_valid_age= 22 <= age <=30
    is_not_ MBA = program.lower() != "MBA"
    
    return is_valid_age and is_not_MBA\
    
    age = int(input("Enter your age: "))
    program = input("Enter your program: ")
    
    result = check_age_and_program(age, program) 
    
    if result: 
          print("You met the criteria.")
    else: 
          print("You do not meet the criteria.")
          
          