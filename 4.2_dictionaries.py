"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a dictionary describing one customer, written in the code.
# 2. Process: Python reads some fields, changes one, removes one,
#    then goes through every field. It also asks for a field that does not exist.
# 3. Out: each field with its value, before and after the changes.
# 4. My object, my five fields, and why those:
#    a customer of an online shop. name and email to contact them,
#    city to target local offers, loyalty_points to reward them,
#    last_purchase to know what to recommend next.


# Your code below
# My customer, described with a dictionary: field name -> value
customer = {
    "name": "Carla Martin",
    "email": "carla.martin@mail.com",
    "city": "Paris",
    "loyalty_points": 120,
    "last_purchase": "sneakers"
    }

# Read some fields
print("The customer's name is: ", customer["name"])
print("The customer's city is: ", customer["city"])

# Change a field: the customer earned 30 more points
customer["loyalty_points"] = customer["loyalty_points"] + 30
print("The customer's points are now: ", customer["loyalty_points"])

# Remove a field: the city is not needed anymore
customer_city = customer.pop("city")
print("The removed city was: ", customer_city)

# Display every remaining field with its value
for field, value in customer.items():
    print(field, ":", value)

# Ask for a field that does not exist, without crashing
print("The customer's phone is: ", customer.get("phone", "not available"))

# Check:
# - With customer["phone"], the program crashed with KeyError: 'phone',
#   because this field is not in the dictionary.
# - With customer.get("phone", "not available"), it survives
#   and displays "not available".