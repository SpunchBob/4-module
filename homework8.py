# class Item:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand

#     def __repr__(self):
#         return self.brand
    
# items_list = [
#     Item(1000, "Apple"),
#     Item(1200, "Apple"),
#     Item(900, "Sumsung"),
#     Item(700, "Sumsung"),
#     Item(660, "Xiaomi")
# ]
# print(filter(lambda item: item("Apple"), items_list))

names_list = ['данил', 'артём', 'никита', 'влад']
result = [(lambda x: x.capitalize())(x) for x in names_list]
print(result)