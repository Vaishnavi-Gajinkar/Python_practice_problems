'''Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days '''

import calendar
from datetime import date

sd = input("Enter start date (Format YYYY,MM,DD) ")
# ed = input("Enter end  date (Format YYYY,MM,DD) ")
# f_dt = sd.replace("/",",")  #.split("/")
initial = date(sd)
print(initial)

