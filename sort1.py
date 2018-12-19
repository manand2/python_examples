# sort elements in a class instances

from operator import(attrgetter

class Employee():
 
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


    def __repr__(self):
        return '(name is {}, age is{}, salary is {}'.format(self.name,self.age,self.salary)

# initialize employees information         
  e1 = Employee('Carl', 21, 70000)
  e2 = Employee('Sarah', 23, 80000)
  e3 = Employee('Bob', 33, 100000)

# make a list of employees

 employees = [e1,e2,e3]

 def e_sort(emp):
    return emp.name

 s_employees = sorted(employees,key=e_sort)

# lamda function - quickly write anonymous functions

s_employees = sorted(employees, key=lambda e: e.name)

# another way
from operator import(attrgetter

s_employees = sorted(employees, key=attrgetter('age'))
