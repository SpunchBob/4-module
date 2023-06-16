goods = [
    {
        "name":"Iphone7",
        "brand": "Apple",
        "price": 25000
    },
    {
        "name": "Ipad",
        "brand": "Apple",
        "price": 35000
    },
    {
        "name": "Windows XP",
        "brand": "Microsoft",
        "price": 1500
    }
]

def price(item):
    return item['price']

print(sorted(goods, key=lambda item: item['price']))
filter_list = list(filter(lambda item: item["brand"] == "Apple", goods))
print(filter_list)

numbers = ['1', '2', '3', '4', '5']

result = list(map(int, numbers))
print(result)
print(type(result))

names = ['Igor', 'Артём', 'Аня', 'Ксюша']
surnames = ['Иванов', 'Петрович', 'Максимова', 'Андреевна']

persons = list(map(lambda name, surname: f'{name}, {surname}', names, surnames))
print(persons)

new_goods = []

for index, item in enumerate(goods):
    print(index)
    new_goods.append({index: item})

print(new_goods)

names = ['Igor', 'Артём', 'Аня', 'Ксюша']
surnames = ['Иванов', 'Петрович', 'Максимова', 'Андреевна']

for name, surname in zip(names, surnames):
    print(name, surnames)

print(__name__)