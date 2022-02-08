#secondstring.py
#this program asks for a string and outputs every second character in reverse order
#author: Roberto Vergano

print("Welcome to the Reversator!")

#Line 8 asks the user to enter a sentence. "str" specifies that the sentence introduced is text type.
a = str(input("Please enter a sentence: "))

#Line 12 will reverse the string "a". 
#[::-1] takes the string from -1 (first character from the right), and it reverses it (we do not indicate length so the program reverses the whole string)
b = a[::-1]

#Line 15 outputs the sentence reversed in a new line using "\n"
print ("Your sentence reversed is: \n" +b) 

#Line 18 creates an empty string. We are going to use it to create a loop.
c = "" 
#Line 21, "len(b)" returns the length of the reversed sentence. "range" creates a sequence of numbers based on the value of "len(b)"
#With "for i in" we are creating an index that covers this sequence of numbers i = [1,2,3,4,5,6,7,8,9,...]
for i in range(len(b)):
    #Line 25, we use the operator "%" to calculate the remainder "for" every value in "i"/2. "if" the remainder is zero, it means that is an even number. 
    # A remainder "0"(e.g.4/2 Remainder = 0) is a FALSE statement. zero not iqual to (!=0) zero -> FALSE. 
    # Only even values give a FALSE statement, so they can exit the loop. 
    if i%2 !=0:
        #Line 27, since "c" is an empty string, it will only have an output each time an even value exists the loop, which corresponds to a character in the reverse sentence.
        c = c + b[i]      

#Finally, Line 30 will output every second character in reverse order from the input sentence.
print ("Every second letter in reverse order: \n" + c)




        

