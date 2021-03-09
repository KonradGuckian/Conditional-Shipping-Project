weight = 4.8
premiumrate = 125.00
#Ground Shipping
if weight <= 2:
  costground = weight * 1.50 + 20.00
elif weight <= 6:
  costground = weight * 3.00 + 20.00
elif weight <= 10:
  costground = weight * 4.00 + 20.00
else:
  costground = weight * 4.75 + 20.00

print(f'Ground shipping cost: ${costground}')

#premium ground shipping
print(f'Cost of shipping Ground Premium: ${premiumrate}')

#Drone shipping
if weight <= 2:
  dronecost = weight * 4.50
elif weight <= 6:
  dronecost = weight * 9.00
elif weight <= 10:
  dronecost = weight * 12.00
else:
  dronecost = weight * 14.25
print(f'Cost of shipping with drone: ${dronecost}')
