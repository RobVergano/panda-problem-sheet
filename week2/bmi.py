#bmi.py
#This program calculates the BMI
#Author: Roberto Vergano

#BMI=Kg/(m)^**2
# Kg = Variable weight
# m = Variable height

#Line 9 to make an introduction user friendly.
print ("Welcome to BMI Calculator!")

#line 13 and 14 asks the user for weight and height. int assigns a numeric value to the variable. float function converts the variable in a float number in case the user enters a decimal number.
weight = int(float(input("Enter your weight (Kg): ")))
height = int(float(input("Enter your height (cm): ")))

#line 17 to change from cm to m
heightm = height/100

#line 20 calculates the BMI with the values of line 13 and 17
BMI =(weight/(heightm)**2)

#Line 23, using the round function we output only 2 decimals.
value = round(BMI,2)

#Line 26 outputs the result. We use "str" to change the variable from numerical to text type.
print ("Your BMI is " + str(value))

# Usinf if, elif and else function we create a range of values according to the BMI. 
if value < 18.5:
    print ("Underweight")
elif value <24.9:
    print ("Healthy weight")    
elif value <29.9:
    print("Overweight")
else:
    print ("Obesity")

