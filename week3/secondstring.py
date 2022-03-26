#secondstring.py
#this program asks for a string and outputs every second character in reverse order
#author: Roberto Vergano




print("Welcome to the Reversator!")

#Line 8 asks the user to enter a sentence. "str" specifies that the sentence introduced is text type.
a = str(input("Please enter a sentence: "))

#Line 12 will reverse the string "a". 
#[::-1] takes the string from -1 (first character from the right), and it reverses it (we do not indicate length so the program reverses the whole string)
b = a[::-1]

#Line 21 creates an empty string which it is used to include the loop.
#Line 22, Len function returs the number of characters in the string. Using range function we create a sequence of numbers from the reversed string.
#Line 23, we divide every number by 2, if the remainder is iqual to zero , then character exits the loop.

c = "" 
for i in range(len(b)):
       if i%2 ==0:
               c = c + b[i]              

#Finally, Line 27 will output every second character in reverse order from the input sentence.
print (c) 

