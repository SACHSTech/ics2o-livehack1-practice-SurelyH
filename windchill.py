'''
-------------------------------------------------------------------------------
Name:		windchill.py
Purpose:  Hours to days

Author:	Huang.S

Created:	date in 03/12/2020
------------------------------------------------------------------------------
'''

# input temperature and wind print
temperatureC = float(input("Enter the temperature in Celsius: "))
wind_speed = float(input("Enter the wind speed in km per hour: "))

# calculation of wind chill factor
wind_chill_factor = (13.12 + (0.6215 *temperatureC) - (11.37 *wind_speed**0.16) + (0.3965 *temperatureC *wind_speed**0.16))

#output
print("When the temperature reaches " + str(temperatureC) + " degrees Celsius, and the wind speed being " + str(wind_speed) + "km/h, the wind chill will be " + str(wind_chill_factor) + " degrees Celsius.")