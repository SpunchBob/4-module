class Employee:
    def __init__(self, name, salary, is_good_employee):
        self.name = name
        self.salary = salary
        self.is_good_employee = is_good_employee


first_employee = Employee(name="Александр", salary=20000, is_good_employee=True)
second_employee = Employee(name="Шура", salary=20000, is_good_employee=False)
third_employee = Employee(name="Сашок", salary=20000, is_good_employee=True)
fourth_employee = Employee(name="Саня", salary=20000, is_good_employee=True)

employeers = [first_employee, second_employee, third_employee, fourth_employee]
counter = 0
for i in employeers:
    counter += 1
    if i.is_good_employee != True:
        employeers.pop(counter)

print(employeers)

