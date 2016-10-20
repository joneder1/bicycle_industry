class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    def __repr__(self):
        return "{0} has ${1} to spend on a new bicycle".format(
            self.name, self.budget)

class Bicycle(object):
    def __init__(self, model_name, weight, cost):
        self.model_name = model_name
        self.weight = weight
        self.cost = cost
    def __repr__(self):
        #price is bike cost + bike markup
        return "The {0} weighs {1} lbs and costs ${2}".format(
            self.model_name, self.weight, self.price)

class Bike_Shop(object):
    def __init__(self, name, profit_margin, bikes):
        self.name = name
        self.profit_margin = profit_margin
        self.profit = 0
        self.inventory = {}
        for bike in bikes:
            #markup is x = (bike price / 100) * (profit margin) 
            bike.markup = int((bike.cost / 100) * self.profit_margin)
            bike.price = bike.cost + bike.markup
            #inventory is the bike models names - how to make each bike model have a different total # of inventory?
            self.inventory[bike.model_name] = bike
            
    def __repr__(self):
        template = "The bike shop {0} has made ${1} in profit.\n \nCurrent inventory:\n{2} \n"
        # "\n" put a line break after each string returned, lists the bike model names
        # values() returns a list of all the values available in a given dictionary.
        bikes = "\n".join(str(bike) for bike in self.inventory.values())
        return template.format(self.name, self.profit, bikes)
    
    def can_afford(self, budget):
        bikes = self.inventory.values()
        # returns list of bikes where bike price total must be less than or equal to customer budget
        return [bike for bike in bikes if bike.price <= budget]

    def sell(self, bike, customer):
        customer.bike = bike
        #removes the bike.price from customer.budget, leaves remaining customer budget
        customer.budget -= bike.price
        #adds the markup to self.profit
        self.profit += bike.markup
        #remove bike that has been purchased
        del self.inventory[bike.model_name]

