# class Example:
#     def __init__(self):
#         print("Hello from Constructor")

#     def sayHello(self):
#         print("Hello world")

# ob1 = Example()
# ob1.sayHello()


# class Car:
#     def __init__(self, color):
#         self.carColor = color

#     def getColor(self):
#         print(f"The color of the car is {self.carColor}")

# car1 = Car("Red")
# car2 = Car("Blue")

# car1.getColor()
# car2.getColor()


class Animal:
    def __init__(self, name="Unknown"):
        self.name = name

    def getName(self):
        print(f"The name of the animal is {self.name}")

dog = Animal("Dog")
dog.getName()

cat = Animal()
cat.getName()

# 15. Write a program to create a list of prime numbers between 1 and 100.