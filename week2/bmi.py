#bmi.py
#This program calculates the BMI
#Author: Roberto Vergano

#BMI=Kg/(m)^**2
# Kg = Variable weight
# m = Variable height

print ("Welcome to BMI Calculator!")
#Line 9 to make it more user friendly.
weight = int(input("Enter your weight (Kg): "))
height = int(input("Enter your height (cm): "))
#line 11 and 12 asks the user for weight and height. int assigns a numeric value to the variable.
heightm = height/100
#line 14 to change from cm to m
BMI = str(weight/(heightm)**2)
#line 16 calculates the BMI with the values of line 11 and 14
print ("Your BMI is " + BMI)
#line 18 prints the value of the BMI
value = int(float(BMI))
if value < 18.5:
    print ("Underweight")
elif value <24.9:
    print ("Healthy weight")    
elif value <29.9:
    print("Overweight")
else:
    print ("Obesity")

