secondstring.py
The program is designed to reverse a sentence and output every second character of that sentence.

To do that:
1. We defined the input sentence ("a") as a text type using "str"
2. This string is reversed using "[::-1]", this assigns as a first character the first one from the right in the string.
3. Once the string is reversed ("b") we create an empty string called "c".
4. For "c", we define the length of "b" (len(b)) and using "range" we will create a sequence of numbers based on the value of len(b)
5. For this sequence "i", we will create a loop, which only allows the exit of even numbers. 
6. This loop divides each number in "i" by 2. A remainder equal to zero means that i is an even number.
7. "==0"(equal to) will be the condition to exit the loop.
8.  This number is converted back to the character according to the position hold in the sequence "b[i]"
9. This gives a value to "c" which we output.
10. The program runs this loop for every value in the range until the sequence is finished. 

REFERENCES

https://www.w3schools.com/python/python_howto_reverse_string.asp

https://stackoverflow.com/questions/29002097/empty-string-in-python

https://codippa.com/how-to-print-characters-at-even-position-in-string-in-python/

https://stackoverflow.com/questions/63789505/printing-every-other-letters-of-a-string-without-the-spaces-on-python

https://www.journaldev.com/23647/python-reverse-string








