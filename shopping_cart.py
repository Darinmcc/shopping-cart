# shopping_cart.py

#from pprint import pprint


# additional task add dictionary to capture how many per item
# then p for p in products if p["per tiem"] == per pound
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per":"item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per":"item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per":"item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per":"item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per":"item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per":"item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per":"item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per":"item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per":"item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per":"item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per":"item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per":"item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per":"item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per":"item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per":"item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per":"item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per":"item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per":"item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per":"item"},
    {"id":20, "name": "Bananas", "department": "produce", "aisle": "fruits and vegtables", "price": 0.79, "price_per":"pound"},
    {"id":21, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per":"item"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

def to_time(my_time):
    return "{0:,.0f}".format(my_time)

avail_ids = ["DONE"]

kart = []

subtotal = 0

now = datetime.datetime.now().replace(microsecond=0)

AMPM = now.strftime("%p")

for item in products:
    if item["id"] not in avail_ids:
        avail_ids.append(str(item["id"]))




print("--------------------")
print("Welcome! Start entering items")
print("--------------------")

while ["DONE"] not in kart:
    product_ID = input("Please input a product identifier:")

    if product_ID not in avail_ids:
        print("Hey, are you sure that product identifier is correct? Please try again!")
        exit()

    elif product_ID == "DONE":
        print("GENERATING RECEIPT")
        break
    
    else:
        kart.append(int(product_ID))


print("--------------------")

print("MCCOLLUM FOODS GROCERY")
print("WWW.MCCOLLUM-FOODS-GROCERY.COM")
print("---------------------------------")
print(f"CHECKOUT AT: {now} {AMPM}")
print("---------------------------------")
print("SELECTED PRODUCTS:")


for entries in kart:
    for item in products:
    
        price_usd = to_usd(item['price'])

        if entries == item["id"]:
            subtotal += item['price']
            print(f"...  {item['name']}  {price_usd}")

tax = subtotal * 0.08725

total = subtotal + tax      

usd_subtotal = to_usd(subtotal)
usd_tax = to_usd(tax)
usd_total = to_usd(total)

print("---------------------------------")
print(f"SUBTOTAL: {usd_subtotal}")
print(f"TAX: {usd_tax}")
print(f"TOTAL: {usd_total}")
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")

    
    



# pprint(products)

# TODO: write some Python code here to produce the desired output

#(shopping-env)  --->> python shopping_cart.py
#Please input a product identifier: 1
#Please input a product identifier: 8
#Please input a product identifier: 6
#Please input a product identifier: 8
#Please input a product identifier: 8
#Please input a product identifier: 16
#Please input a product identifier: 12
#Please input a product identifier: DONE
#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2019-06-06 11:31 AM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Dry Nose Oil ($21.99)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Mint Chocolate Flavored Syrup ($4.50)
#>  ... Chocolate Fudge Layer Cake ($18.50)
#> ---------------------------------
#> SUBTOTAL: $61.24
#> TAX: $5.35
#> TOTAL: $66.59
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------


#for item in products:
    #if item["id"] == int(product_ID):
        #print("Is this item correct?" + f"  {item['name']} ... {price_usd}")