# class Year:
#     def __init__(self):
#         self.__days = 365
        
#     def get(self):
#         return self.__days
    
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise ValueError(f"Некоректное значение атрибута: {days}")
        
# year = Year()
# print(year.get())
# year.set_days(366)
# print(year.get())

# class Person:
#     def __init__(self, name, age):
#         self.__name = name 
#         self.__age = age

#     @property 
#     def age(self): #getter
#         return self.__age 
    
#     @age.setter
#     def age(self, age): #setter
#         if age < 0:
#             raise ValueError("Вы ещё не родились, пожалуйста покиньте сайт")
        
#         self.__age = age

# person = Person("Name", 86)
# print(person.age)
# person.age = 56
# print(person.age)

class List:
    def __init__(self, num):
        self.listt = []
        for i in range(num):
            self.listt.append(i)
        return self.listt
    
    def delite(self):
        self.listt[-1] = 0
