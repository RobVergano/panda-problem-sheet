# letter.py
# This program reads in a text file and outputs the number of e´s (or other letter) it contains. 
# Author: Roberto Vergano

print("Welcome to the letter counter!")
#Line 7 and 8 asks the user to input a text file and the letter wanted. 
#The assumption here is that the text file is in the same directory as letter.py, otherwise It must be specified.
a = input("Please enter a text file: ")
b = input("Please enter a letter: ")

#Line 11 defines the function.
def number (a,b):
    #Line 13, we use the function "open"+"r" to open the file for reading.
    file = open(a, "r")
    #Line 15 reads the content from the text file.
    textfile = file.read()
    #Line 17 returns the the number of times the specified value "b" appears in the text file.
    return textfile.count(b)

#Line 22 outputs the number of times the specified letter appears in the text file. 
#Since the output of "textfile.count" is a numerical value we have to convert it into a string.
print("The number of letters {} in {} is ".format(b,a) + str(number(a,b)))




