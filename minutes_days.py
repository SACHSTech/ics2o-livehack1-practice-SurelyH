'''
-------------------------------------------------------------------------------
Name:		minutes_days.py
Purpose:  Minutes to days, hours, and minutes

Author:	Huang.S

Created:	date in 03/12/2020
------------------------------------------------------------------------------
'''

# input of number of minutes
minutes = float(input("Enter the number of minutes: "))

# changing minutes to days, hours, and minutes
days = (minutes // 1440)
extra_minutes = (minutes % 1440)
hours = (extra_minutes // 60)
final_minutes = (extra_minutes - hours *60)

# output in days, hours, and minutes
print("The number of days would be " + str(days) + " day(s), " + str(hours) + " hour(s) and, " + str(final_minutes) + " minute(s)")