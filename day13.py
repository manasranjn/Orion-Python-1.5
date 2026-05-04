# 4. Hirarchical Inheritance
# class A:
#     def getName(self):
#         print("A")

# class B(A):
#     def sayHello(self):
#         print("Hello")

# class C(A):
#     def greet(self):
#         print("Hi")

# class D(A):
#     def getName(self):
#         print("D")

# b1 = B()
# b1.sayHello()
# b1.getName()

# c1 = C()
# c1.greet()
# c1.getName()

# 5. Hybrid Inheritance
# class A:
#     def getName(self):
#         print("A")

# class B(A):
#     def sayHello(self):
#         print("Hello")

# class C(B):
#     def greet(self):
#         print("Hi")

# class D(A):
#     def getName(self):
#         print("D")

# b1 = B()
# b1.sayHello()
# b1.getName()

# c1 = C()
# c1.greet()
# c1.getName()

class Animal:
    def __init__(slef, name):
        slef.name = name
    
    def getName(self):
        print(self.name)

class Dog(Animal):
    def getName(self):
        print("This is a DOG")

d1 = Dog("Dog")
d1.getName()

a1 = Animal("Dog")
a1.getName()