# shopping_cart.py

#products = [
#    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
#    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
#    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
#    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
#    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
#    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
#    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
#    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
#    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
#    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
#    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
#    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
#    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
#    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
#    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
#    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
#    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
#    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
#    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
#    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
#    {"id":21, "name": "Bananas", "department": "fruit and vegetable", "aisle": "fruit", "price": 0.79, "price_per": "pound"},
#    {"id":22, "name": "Apples", "department": "fruit and vegetable", "aisle": "fruit", "price": 1.29, "price_per": "pound"},
#    {"id":23, "name": "Sliced Turkey", "department": "deli", "aisle": "poultry counter", "price": 6.99, "price_per": "pound"}
#] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# Program utilizes to_usd function provided by Professor Rossetti to convert values to USD format
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# Import os to read variables from .env file
# Import requirements for sendgrid to enable emailing receipts
import os
from dotenv import load_dotenv
from pandas import read_csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

# Read products.csv file to create DataFrame
csv_filepath = "products.csv"
products_df = read_csv(csv_filepath)

products = products_df.to_dict("records")


# Create list of valid IDs against which to compare user input
# When creating list, covert values from int to str to enable comparison with user input
valid_ids = []
for identifier in products:
    valid_ids.append(str(identifier["id"]))

# Create list of IDs with prices per pound
price_per_pound = []
for identifier in products:
    if(identifier["price_per"] == "pound"):
        price_per_pound.append(str(identifier["id"]))

# Welcome user and provide instructions on how to use the app
print("Hello, welcome to Green Foods Grocery's cehckout application!")
print("---------------------------------")
print("You will be prompted to enter the product identifiers for each product.")
print("When you are done entering all product identifiers, enter 'DONE'.")
print("---------------------------------")


# Capture product IDs until user is finished using an infinite while loop using modified code based on that provided in class
# If user enters a product that is priced per pound, prompt user to indicate number of pounds and add value to pounds list
selected_ids = []
pounds = []
while True:
    selected_id = input("Please input a product identifier: ")
    if selected_id.upper() == "DONE":
        break
    else:
        # Verify that the product ID is valid
        if(selected_id in valid_ids):
            if(selected_id in price_per_pound):
                # Error handling to ensure input provided by user is a valid number
                # Utilized Python documentation for error handling code (https://docs.python.org/3/tutorial/errors.html)
                try:
                    lbs = float(input("How many pounds? "))
                    pounds.append(float(lbs))
                    # If valid, append to the selected_ids list
                    selected_ids.append(selected_id)
                except ValueError:
                    print("Oops! That was not a valid number. Please re-enter the product identifier to try again.")
            else:
                selected_ids.append(selected_id)
        # If it is not valid, print "Are you sure that product identifier is correct? Please try again!" 
        # and return to beginning of while loop
        else:
            print("Are you sure that product identifier is correct? Please try again!")     
print("---------------------------------")

# Ask user if they want an email receipt
while True:
    email_receipt = input("Would you like your receipt via email? Please enter 'y' for yes or 'n' for no: ")
    email_address = ""
    if(email_receipt == "y"):
        # Prompt user to provide email address to which the receipt will be sent
        email_address = input("Please enter the email address to which you would like the receipt to be sent: ")
        print("Ok, we will send an email receipt to ", email_address)
        break
    elif(email_receipt == "n"):
        print("Ok, we will not send a receipt via email.")
        break
    else:
        print("We're sorry, that input was invalid. Please try again!")


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
counter = 0
html_list_items = []
for id in selected_ids:
    # Display the selected product's name and price
    matching_products = [p for p in products if str(p["id"]) == str(id)]
    matching_product = matching_products[0]
    
    if(matching_product["price_per"] == "pound"):
        #print("THIS PRODUCT IS PRICED PER POUND!")
        #print("COUNTER:", counter)
        #print("POUNDS[COUNTER]:", pounds[counter])
        subtotal += float(matching_product["price"]) * pounds[counter]
        price = to_usd(float(matching_product["price"]) * float(pounds[counter]))
        counter = counter + 1
    else:
        subtotal += float(matching_product["price"])
        price = to_usd(matching_product["price"])
    print(" ...", matching_product["name"], f"({price})")
    html_list_items.append(f'{matching_product["name"]}, ({price})')


# Print subtotal
print("---------------------------------")
subtotal_usd = to_usd(subtotal)
print("SUBTOTAL:", subtotal_usd)

# Print tax and total with tax (sum of subtotal and tax) using tax rate specified in .env file
# Need to convert TAX_RATE from .env file from str to float before performing multiplication with subtotal
tax = subtotal * float(TAX_RATE)
tax_usd = to_usd(tax)
print("TAX:", tax_usd)

total_usd = to_usd(subtotal+tax)
print("TOTAL:", total_usd)
print("---------------------------------")


# Send email receipt
# Modified code provided by Professor Rossetti (link below)
# https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

#for item in html_list_items:
#    print(item)

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>

subject = "Your Receipt from the Green Grocery Store"

html_content = f"""
<h3>Your Receipt from the Green Grocery Store</h3>
<p>WWW.GREEN-FOODS-GROCERY.COM</p>
<p>------------------------------------------------</p>
<p>CHECKOUT AT: {timestampStr}</p>
<p>------------------------------------------------</p>
<p>ITEMS PURCHASED:</p>
<ol>
    {html_list_items}
</ol>
<p>------------------------------------------------</p>
<p>SUBTOTAL: {subtotal_usd}</p>
<p>TAX: {to_usd(tax)}</p>
<p>TOTAL: {to_usd(subtotal+tax)}</p>
"""

message = Mail(from_email=SENDER_ADDRESS, to_emails=email_address, subject=subject, html_content=html_content)

try:
    response = client.send(message)

    #print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    if(response.status_code == 202):
        print("Email receipt sent successfully!")
    #print(response.status_code) #> 202 indicates SUCCESS
    #print(response.body)
    #print(response.headers)

except Exception as err:
    print("No email receipt sent.")
    #print(type(err))
    #print(err)


# Display thank you message to user
print("---------------------------------")
print("Thank you! See you again soon!")
print("---------------------------------")

