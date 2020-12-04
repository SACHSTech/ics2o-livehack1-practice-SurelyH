'''
-------------------------------------------------------------------------------
Name:		days_hours.py
Purpose:  Hours to days

Author:	Huang.S

Created:	date in 03/12/2020
------------------------------------------------------------------------------
'''

# input number of hours
hours = float(input("Enter the number of hours: "))

# changing hours to days
days = (hours // 24)
extrahours = (hours % 24)

# output of days + hours
print("The number of days would be " + str(days) + " day(s) and " + str(extrahours) + " hour(s)")