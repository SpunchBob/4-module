class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other
    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(self, other):
            return self.price - other
    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(self, other):
            return self.price * other
    def __floordiv__(self, other):
        if isinstance(other, Item):
            return self.price // other.price
        elif isinstance(self, other):
            return self.price // other

item1 = Item("Интел", 15600, 0.65)
item2 = Item("Видюха", 75000, 65)

total_sum = item1 + item2
print(total_sum)

total_sub = item1 - item2
print(total_sub)

total_mul = item1 * item2
print(total_mul)

total_floordiv = item1 // item2
print(total_floordiv) 