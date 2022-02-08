secondstring.py
The program is designed to reverse a sentence and output every second character of that sentence.

To do that:
1. We defined the input sentence ("a") as a text type using "str"
2. This string is reversed using "[::-1]", this assigns as a first character the first one from the right in the string.
3. Once the string is reversed ("b") we create an empty string called "c".
4. For "c", we define the length of "b" (len(b)) and using "range" we will create a sequence of numbers based on the value of len(b)
5. For this sequence "i", we will create a loop, which only allows the exit of even numbers. 
6. This loop divides each number in "i" by 2. A remainder equal to zero means that i is an even number.
7. "!=0"(not equal to) will be the condition to exit the loop. "zero not iqual to zero" is a False statement.
8. A false statement allows the even number exit the loop.
9. This even number is converted back to the character according to the position hold in the sequence "b[i]"
10. This gives a value to "c" which we output.
11. The program runs this loop for every value in the range until the sequence is finished. 

This way we get the second or even characters of the input sentence.