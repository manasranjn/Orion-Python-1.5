# print("Hello Everyone")
# print("Welcome to Python Programming")

l1 = [1, 2, 3, 4, 5]

# for i in l1:
#     print(i)

# s = "Hello Everyone"
# for i in s:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(2,20, 3):
#     print(i)

# for i in range(1,20):
#     if i % 2!=0:
#         print(i)

# for i in range(2,20,2):
#     print(i)

# while loop
# a = 0
# while a> 10:
#     print(a)
#     a+=1

# Write a program to check even number or odd number

# n = int(input("Enter a number: "))
# print(type(n))
# if n % 2 == 0:
#     print("Even Number")
# else:    
#     print("Odd Number")

# WAP to print even or odd from 1 to n
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 2 == 0:
#         # print(i, "Even Number {i}")
#         print(f"{i} Even Number")
#     else:    
#         print(f"{i} Odd Number")


name = "Smith"
age = 20
address = "New York"
# print("Hello, My name is", name, "I am", age, "years old and I live in", address)
# print(f"Hello, My name is {name}, I am {age} years old and I live in {address}")

# count = 0
# for i in range(0,5):
#     for j in range(0,5):
#         for k in range(0,5):
#             print(i, j, k)
#             count += 1

# print("Total Iterations: ", count)

# for i in range(20):
#     print(i)
#     if i == 2:
#         break

for i in range(20):
    if i == 2:
        continue
    print(i)
    
# for i in range(20):
#     pass