# python weekday.py
# this program outputs whether or not is a weekday.
# author: Roberto Vergano

#Line 6 and 7 to import the modules for calendar and datetime
import calendar
import datetime

#Line 10 gives the date as a numerical value which it is converted into str
todaydate = str(datetime.date.today())

#Line 12 imports the day of the week from the datetime module
from datetime import datetime
#Line 15 outputs the day of the week plus the date
print ("Today is " + (datetime.today().strftime("%A ")) + todaydate) 

#Line 18 imports the day of the week as a number, Monday = 0; Tuesday =1;...; Sunday = 6
from datetime import datetime
#Line 20 creates the variable for the number obtained. 
day = (datetime.today().weekday())

#Line 23 and 25, using a conditional, only when the value is 5 or 6 (Saturday or Sunday) the program outputs "It is the weekend"
if day <=4:
    print ("Yes, unfortunately today is a weekday")
else:
    print ("It is the weekend, yay!")











