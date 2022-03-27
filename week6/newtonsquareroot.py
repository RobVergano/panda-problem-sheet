#pythonsquareroot.py
#Using the newton´s method, this program takes a positive floating number as input and outputs an approximation of its square root.
#Author: Roberto Vergano

print ("Welcome to the squarerooter!")

#Line 8 defines the variable "n". Using "int" and "float" we define the variable as a numerical value and float number.
n = int(float((input("Enter a positive number = "))))

#Line 10. We define the following function.
def newton(n):
    #Line 13, we assume the best value is approximately half of the number "n".
    a = 0.5*n
    #Line 15, using the newton´s method we ask the program to find a better value.
    b = 0.5*(a +n/a)
    #Line 17, we loop this process, while "b" is not equal to the aproximated number "a"
    while b !=a:
        #Line 19, we assume the best value from "b" will be closest approximation to "a"
        a = b
        #Line 21, we repeat this process until the program cannot get a better value. Then we output this value. 
        b = 0.5*(a + n/a)
    return a

print ("The square root is ", newton(n))
