# 1. Print all numbers divisible by 3 between 1 to 30.
# 2. Find square root using math module.
# 3. Generate random number between 1 to 10.
# 4. Print current date
# 5. Print prime numbers between 1 to 100
# 6. Check Armstrong number
# 7. Sort words alphabetically

# 2. Find square root using math module.
# import datetime
# print(datetime.date.today())


# 6. Check Armstrong number
# num = 153
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3 #27 + 125 + 1 = 153
#     temp //= 10 # 153 // 10 = 15, 15 // 10 = 1, 1 // 10 = 0
# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")


# Encapsulation
# class Person:
#     def __init__(self, name, age, address):
#         self.name = name # public variable
#         self._age = age # protected variable
#         self.__address = address # private variable

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self._age}")
#         print(f"Address: {self.__address}")


# person1 = Person("John", 25, "123 Main St")
# print(person1.name)
# print(person1._age)
# print(person1.__address)
# person1.display()

# class Student(Person):
#     def show(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self._age}")
#         print(f"Address: {self.__address}") # not possible/error

# s1 = Student("John", 25, "123 Main St")
# # s1.display()
# s1.show()

# Abstraction
# from abc import ABC, abstractmethod
# class Employee(ABC):
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     @abstractmethod
#     def calculate_salary(self):
#         pass

#     @abstractmethod
#     def display_details(self):
#         pass

# class Manager(Employee):
#     def calculate_salary(self):
#         print(f"Your anual Salary is {self.salary*12}")

#     def display_details(self):
#         print(f"Employee name is {self.name}")
#         print(f"Employee salary is {self.salary}")

# e1 = Manager("John", 50000)
# e1.calculate_salary()
# e1.display_details()