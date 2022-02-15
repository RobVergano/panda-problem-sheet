# python collatz.py
# This program asks the user to input any positive integer and outputs the succesive values.
# In each calculation the program even numbers are divided by two, and odd numbers multiplied by 3 and added 1.
# The program ends when current value is one.
# Author: Roberto Vergano

#Line 8 asks the user to enter a number. "int" assigns a numerical value to "n"
n = int(input("Please enter a positive number: "))

#Line 11 runs a loop, if the number introduced is iqual to 1. It asks the user for a new number.
while n == 1:
  print ("Please enter a positive number bigger than 1") 
  n = int(input("Please enter a positive number: "))
  #However, line 15, if the user inputs again the number 1 the program picks a random number.
  if n==1:
      import random
      n = random.randint (2,100)
      print ("Sorry I had to pick for you")

#Line 20 runs another loop, if the number is less or equal to zero. Then it asks the user to introduce a new number until is bigger than 1.
while n<=0:
  print ("That is not a valid number. Please enter a number bigger than 1")
  n = int(input("Please enter a positive number: "))
  #Line 25, if the user tries again number 1 then it will be required to input a new number.
  if n == 1:
    print ("Please enter a number different to one")
    n = int(input("Please enter a positive number bigger than 1: "))
    #Line 29, if user insists in number 1, then the program will pick a random number.
    if n==1:
      import random
      n = random.randint (2,100)
      print ("Sorry I had to pick for you")

#Line 35, only when the previous conditions do not apply the system prints the input number by the user.
print(n)

#Line 38, the program runs a loop as long as the number obtained is not iqual to 1.
while n !=1:
  #Line 40, if the number is even, the remainder will be equal to zero. Then the number is divided by 2.
    if n%2 == 0:
     n = n//2
     print (n)
  #Line 44, however if the previous statement is False, then the system checks if the number is odd.
    elif n%2 !=0:
      #Line 46, if the number is odd, then it will calculate (n*3)+1 and output the result.
      n = n*3+1
      print (n)

# The loop continues until the number is equal to 1. Then stops and prints END.       
if n ==1:
  print ("END")

