#Write a Python program to convert a string to datetime 
from datetime import datetime
date_object = datetime.strptime('Jul 9 2021 6:00PM', '%b %d %Y %I:%M%p')
print(date_object)


#Write a Python program to subtract five days (last working day) from current date
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('\nCurrent Date :',date.today())
print('Five days before Current Date :',dt)


#Write a Python program to convert the date to datetime using a function 
from datetime import date
from datetime import datetime
dt = date.today()
print('\nDatetime :',datetime.combine(dt, datetime.min.time()))


#Write a Python program to print next 7 days (week) starting from today
import datetime
base = datetime.datetime.today()
for x in range(0, 7):
      print('\nNext seven days :',base + datetime.timedelta(days=x))
	  