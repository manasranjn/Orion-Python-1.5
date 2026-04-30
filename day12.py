# # # Inheritance
# class Animal:
#     def __init__(self):
#         print("Animal created")

#     def whoAmI(self):
#         print("Animal")

#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def created(self):
#         print("Dog created")

# d1 = Dog()
# d1.created()
# d1.whoAmI()
# d1.eat()


# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def showDetails(self):
#         print(f"The color of the car is {self.color}")
#         print(f"The model of the car is {self.model}")

# class Sedan(Car):
#     def created(self):
#         print("Sedan created")

# s1 = Sedan("Red", "Sedan")
# s1.showDetails()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getName(self):
#         print(f"The name of the person is {self.name}")

#     def getAge(self):
#         print(f"The age of the person is {self.age}")

# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary

#     def getSalary(self):
#         print(f"The salary of the employee is {self.salary}")

# e1 = Employee("John", 25, 50000)
# e1.getName()
# e1.getAge()
# e1.getSalary()

# Types of Inheritance
# 1. Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print(f"The name of the parent is {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def getAge(self):
        print(f"The age of the child is {self.age}")

c1 = Child("John", 25)
c1.getName()
c1.getAge()

# 2. Multilevel Inheritance
class GrandParent:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print(f"The name of the grandparent is {self.name}")

class Parent(GrandParent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def getAge(self):
        print(f"The age of the parent is {self.age}")

class Child(Parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def getGrade(self):
        print(f"The grade of the child is {self.grade}")

c1 = Child("John", 25, "A")
c1.getName()
c1.getAge()
c1.getGrade()

p1 = Parent("John", 25)
p1.getName()
p1.getAge()

# 3. Multiple Inheritance
class A:
    def getName(self):
        print("A")

class B:
    def getName(self):
        print("B")

class C:
    def getName(self):
        print("C")

class D(A, B, C):
    def getName(self):
        print("D")

d1 = D()
d1.getName()