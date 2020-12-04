'''
-------------------------------------------------------------------------------
Name:		f_to_c.py
Purpose:  Inputing weather in fahrenheit and changing it to celsius

Author:	Huang.S

Created:	date in 03/12/2020
------------------------------------------------------------------------------
'''

# inputing fahrenheit
fahrenheit = float(input("Enter degree in fahrenheit: "))

# calculations
celsius = (5 /9 *(f -32))

# output in celsius 
print("The degree in celsius would be " + str(celsius) + "°C")