''' Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module. '''

import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
print(calendar.month(yy, mm))