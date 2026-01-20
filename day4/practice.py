# design and create an online store for products(name , price).

# track total products being created.

# create a static method to calculate discount on a product based on a given percentage.


class product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        product.count += 1

    def get_info(self):
        print("price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total product in a store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"the discounted price is {price -(price*discount)/100 }")


p1 = product("laptop", 50_000)
p2 = product("phone", 10_000)
p3 = product("pen", 10)

product.get_count()

p1.calc_discount(10_000, 12)
