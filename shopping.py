# Sal's Shipping

# Weight to ship
weight = 0

# Ground shipping prices
ground_shipping_price = 0

if weight <= 2:
  ground_shipping_price += 1.5 * weight + 20
elif weight <= 6:
  ground_shipping_price += 3 * weight + 20
elif weight <= 10:
  ground_shipping_price += 4 * weight + 20
else:
  ground_shipping_price += 4.75 * weight + 20

# Ground shipping premium price
ground_shipping_premium_price = 125

# Drone shipping price
drone_shipping_price = 0

if weight <= 2:
  drone_shipping_price += 4.50 * weight
elif weight <= 6:
  drone_shipping_price += 9 * weight
elif weight <= 10:
  drone_shipping_price += 12 * weight
else:
  drone_shipping_price += 14.25 * weight

# Calculating and printing the cheapest method
cheapest = ""
cheapestprice = 0

if weight <= 0:
  print("Please set up a valid weight.")
else:
  if (ground_shipping_price < ground_shipping_premium_price) and (ground_shipping_price < drone_shipping_price):
    cheapest = "Ground Shipping"
    cheapestprice = ground_shipping_price
  elif (ground_shipping_premium_price < ground_shipping_price) and (ground_shipping_premium_price < drone_shipping_price):
    cheapest = "Ground Shipping Premium"
    cheapestprice = ground_shipping_premium_price
  else:
    cheapest = "Drone Shipping"
    cheapestprice = drone_shipping_price

# Printing out to the user
  print("Ground shipping price: " + str(ground_shipping_price))
  print("Ground shipping premium price: " + str(ground_shipping_premium_price))
  print("Drone shipping price: " + str(drone_shipping_price))

  print("The cheapest method for you is " + cheapest + ", which costs " + str(cheapestprice) + ".")
