# python squareroot.py
# this program takes a positive floating number as input and outputs an approximation of its square root.
# Author: Roberto Vergano

print ("Welcome to the squarerooter!")

#Line 8 defines the variable "n" ans asks the user to input a positive floating number.
n = float(input("Please enter a positive floating number: "))

#Line 11 to create a loop asking the user for a positive number in case a negative number is introduced. 
while n <= 0:
    print ("That is not a positive floating number")
    n = float(input("Please enter a positive floating number: "))
    print (n)

#To find the square root we are going to create a loop.
#Line 22, in this loop we define the variable a.
#Line 25, we are going to multiply "a" for its iqual. 
#Line 26, if the result is within the limits (n-0.0001 < b < n+0.0001), then the program outputs the result (break)
#Line 31, Otherwise, it keeps adding "0.0001" to "a" until the result is within the limits.

a = 0.0001

while (1):
    b = a*a
    if n-0.0001 < b < n+0.0001:
        break
    else:
        #Line 30 "pass" is executed to avoid errors due to empty code.
        pass
        a = a + 0.0001

#Line 34, it outputs the value of "a" which is equal to the square root of "n" and it is rounded up to two decimals.
print ("\nSquare root value is: ",round(a,2))  
       
#This program runs well with small values, however large values slow down the program.

   







