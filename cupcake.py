from abc import abstractmethod
import csv
from pprint import pprint


# PART 1 # =====================================================================

class Cupcake:
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle_type in args:
            self.sprinkles.append(sprinkle_type)
            return self.sprinkles

    @abstractmethod
    def calculate_price(self, quantity):
        return (quantity) * (self.price)



my_cupcake = Cupcake("My Cupcake", "2.99", "chocolate", "cookies n cream", "Oreo pieces", None)
print(my_cupcake.calculate_price(2))

my_cupcake.frosting = "Cream Cheese"
print(my_cupcake.frosting)

my_cupcake.is_miniature = False
print(my_cupcake.is_miniature)

print(my_cupcake.add_sprinkles("Oreo sprinkles, rainbow sprinkles"))
print(my_cupcake.sprinkles)

# PART 2 # =====================================================================


class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, price, flavor, frosting, sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
    

test_cupcake = Mini("Mini Cupcake", "1.99", "chocolate", "vanilla", "rainbow sprinkles")
print(test_cupcake.price)

# PART 3 # =====================================================================

def read_csv(file):
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            pprint(row)

read_csv("sample.csv")

