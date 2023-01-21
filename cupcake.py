from abc import ABC
from abc import abstractmethod
import csv
from pprint import pprint


#  =============1============= #

class Cupcake(ABC):
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



# my_cupcake = Cupcake("My Cupcake", "2.99", "chocolate", "cookies n cream", "Oreo pieces", None)
# print(my_cupcake.calculate_price(2))

# my_cupcake.frosting = "Cream Cheese"
# print(my_cupcake.frosting)

# my_cupcake.is_miniature = False
# print(my_cupcake.is_miniature)

# print(my_cupcake.add_sprinkles("Oreo sprinkles, rainbow sprinkles"))
# print(my_cupcake.sprinkles)

#  =============2============= #

class Mini(Cupcake):
    size = "mini"
    def __init__(self, dinosaur, price, flavor, frosting, sprinkles):
        self.name = dinosaur
        self.price = float(price)
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return (quantity) * (self.price)
    

test_cupcake = Mini("Mini Cupcake", "1.99", "chocolate", "vanilla", "rainbow sprinkles")
print(test_cupcake.calculate_price(5))

#  =============3============= #

def read_csv(file):
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            pprint(row)

read_csv("sample.csv")

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
   
    for cupcake in cupcakes:
                if hasattr(cupcakes, "filling"):
                    writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
                else:
                    writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


dict_cupcake = {"size": "Mini", "name": "Oreo Surpise", "price": "2.99", "flavor": "cookies n cream", "frosting": "oreo", "sprinkles": "chocolate"}

#write_new_csv("cake_storage.csv", test_cupcake)

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
   
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

add_cupcake("cake_storage.csv", test_cupcake)

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)