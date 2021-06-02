# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# Program utilizes to_usd function provided by Professor Rossetti to convert values to USD format
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# Import os to get tax rate from .env file
import os
from dotenv import load_dotenv
load_dotenv()

# Get tax rate from .env file
TAX_RATE = os.getenv("TAX_RATE", default="0.0875")

# Capture date and time at beginning of checkout process
# Code for date and time found on thispointer.com and Stack Overflow for AM/PM (links below)
# https://thispointer.com/python-how-to-get-current-date-and-time-or-timestamp/
# https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-using-strftime
from datetime import datetime
timestamp = datetime.now()
timestampStr = timestamp.strftime("%b-%d-%Y %I:%M %p")


# Create list of valid IDs against which to compare user input
# When creating list, covert values from int to str to enable comparison with user input
valid_ids = []
for identifier in products:
    valid_ids.append(str(identifier["id"]))


# Welcome user and provide instructions on how to use the app
print("Hello, welcome to Green Foods Grocery's cehckout application!")
print("---------------------------------")
print("You will be prompted to enter the product identifiers for each product.")
print("When you are done entering all product identifiers, enter 'DONE'.")
print("---------------------------------")


# Capture product IDs until user is finished using an infinite while loop
selected_ids = []
while True:
    selected_id = input("Please input a product identifier: ")
    if selected_id.upper() == "DONE":
        break
    else:
        # Verify that the product ID is valid. If valid, append to the selected_ids list
        if(selected_id in valid_ids):
            selected_ids.append(selected_id)
        # If it is not valid, print "Are you sure that product identifier is correct? Please try again!" 
        # and return to beginning of while loop
        else:
            print("Are you sure that product identifier is correct? Please try again!")     


# Print top portion of receipt, including timestamp (date and time)
print("---------------------------------")
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")
print("---------------------------------")
# Print timestamp (date and time) of checkout
print("CHECKOUT AT:", timestampStr)
print("---------------------------------")
print("SELECTED PRODUCTS:")

# Perform product lookups to determine each product's name and price
subtotal = 0
for id in selected_ids:
    # Display the selected product's name and price
    matching_products = [p for p in products if str(p["id"]) == str(id)]
    matching_product = matching_products[0]
    #print("...", matching_product["name"], f"({to_usd(matching_product["price"])}))
    subtotal += float(matching_product["price"])
    price = to_usd(matching_product["price"])
    print(" ...", matching_product["name"], f"({price})")

# Print subtotal
print("---------------------------------")
subtotal_usd = to_usd(subtotal)
print("SUBTOTAL:", subtotal_usd)

# Print tax and total with tax (sum of subtotal and tax) using tax rate specified in .env file
# Need to convert TAX_RATE from .env file from str to float before performing multiplication with subtotal (an integer)
tax = subtotal * float(TAX_RATE)
print("TAX:", to_usd(tax))
print("TOTAL:", to_usd(subtotal+tax))

# Display thank you message to user
print("---------------------------------")
print("THANK YOU! SEE YOU AGAIN SOON!")
print("---------------------------------")
