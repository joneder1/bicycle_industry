import random
from bicycles import Bicycle, Bike_Shop, Customer

#bikes name, weight, cost to produce

bikes = [
    Bicycle("Huffy Sledgehammer", 25, 100), Bicycle("State Bicycle", 20, 200),
    Bicycle("Cinelli Gazzetta", 18, 500), Bicycle("All City Thunderdome", 15, 600),
    Bicycle("Bianchi Super Pista", 15, 800), Bicycle("Surly Steam Roller", 25, 400)
    ] 
#shop name, 20% markup, list of bikes 

shop = Bike_Shop("Fast Folks Cyclery", 20, bikes)

#customers name and budget
customers = [Customer("Mike", 200), Customer("Ryan", 500), Customer("Jon", 1000)]

#prints customers as defined in __repr__ from bicycles.py
print(customers, "\n")

for customer in customers:
    #returns customers who can afford certain bikes within their budget
    bikes = ", ".join(bike.model_name for bike in shop.can_afford(customer.budget))
    print (customer.name, "can afford the following bicycles:", bikes)

#The Bike Shop BEFORE sales with current inventory as defined in __repr__
print(shop)

template = "{0} bought the {1} at ${2}, and he has ${3} left over."

for customer in customers:
    #customer buys random bike depending on what they can afford
    will_buy = shop.can_afford(customer.budget)
    shop.sell(random.choice(will_buy), customer)
    
    print(template.format(
        customer.name, customer.bike.model_name,
        customer.bike.price, customer.budget))

#The Bike Shop AFTER selling bikes

print(shop)

