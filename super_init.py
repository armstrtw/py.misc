class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

    def supername(self):
        return super().name

class SalaryEmployeeNosup(Employee):
    def __init__(self, id, name, weekly_salary):
        self.id = id
        self.name = name
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

    def supername(self):
        return self.super().name


print("normal:")
semp = SalaryEmployee(23,"Johnny Redd",40e3)
print(semp.calculate_payroll())
print(semp.name)
print(semp.supername())
print(semp.id)
print("no sup:")
#semp_nosup = SalaryEmployeeNosup(24,"Johnny Nosup",90e3)
#print(semp_nosup.calculate_payroll())
#print(semp_nosup.name)
#print(semp_nosup.supername())
#print(semp_nosup.id)
