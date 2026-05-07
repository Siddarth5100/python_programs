class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        bonus = self.salary * 5 / 100
        return bonus
    
    def display_details(self):
        print(self.name)
        print(self.salary)

class Manager(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 20 / 100
        return bonus
    
    def display_details(self):
        super().display_details()
        print("Role: Manager")
        

class Developer(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 10 / 100
        return int(bonus)

emp = Employee("Arasan", 50000)
# print(emp.calculate_bonus())

man = Manager("Bala", 50000)
# print(man.calculate_bonus())
man.display_details()


dev = Developer("Chandru", 50000)
# print(f"Developer Bonus: {dev.calculate_bonus()}")