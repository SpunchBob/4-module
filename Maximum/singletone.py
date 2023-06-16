# class A:
#     pass

# a1 = A()
# a2 = A()

# print(a1 is a2)
# print(id(a1), id(a2))

class SingleTone():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

a = SingleTone(10, 20)
b = SingleTone(30, 40)
print(a is b)
print(a.a, a.b)
print(a.a, b.b)