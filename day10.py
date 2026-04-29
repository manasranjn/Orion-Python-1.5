# 1. Write a program to take 5 numbers from the user and store them in a list. Print the maximum and minimum.

# lst = []
# for i in range(5):
#     n = int(input("Enter number: "))
#     lst.append(n)

# print("Maximum number is: ", max(lst))
# print("Minimum number is: ", min(lst))

# 2. Create a function is_palindrome(word) that returns True if the string is palindrome, else False.
# def is_palindrome(word):
#     rev = word[::-1]    
#     if word == rev:
#         print(word, "is a palindrome")
#     else:
#         print(word, "is not a palindrome")

# word = input("Enter a word: ")
# is_palindrome(word)

# Create a program to remove duplicate items from a list without using set().
# l1 = [10, 20, 30, 10, 30, 50,40, 50, 60, 70, 80, 90, 100]
# l2 = []

# for i in l1:
#     if i not in l2:
#         l2.append(i)

# print(l2)

# 8. Write a program to find the second largest number in a list.
# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# lst.sort(reverse=True)
# print(lst[1])


# 10. Write a function to return count of each character in a string (use dictionary).
# def char_count(string):
#     count = {}
#     for char in string:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1 # count[h] = 1 
#             # count={h:1, e:1, l:2, o:1}
#     return count

# print(char_count('hello'))


# Modules
# Pre-defined modules

# import math
# print(math.pi)
# print(math.factorial(5))
# print(math.sqrt(25))
# print(math.pow(2,3))
# print(math.log(10))
# print(math.ceil(10.5))

# import math as m
# print(m.pi)
# print(m.factorial(5))
# print(m.sqrt(25))
# print(m.pow(2,3))
# print(m.log(10))
# print(m.ceil(10.5))

# from math import *
# print(pi)
# print(factorial(5))
# print(sqrt(25))
# print(pow(2,3))
# print(log(10))
# print(ceil(10.5))

# from math import pi, factorial, sqrt, pow, log, ceil
# print(pi)
# print(factorial(5))
# print(sqrt(25))
# print(pow(2,3))
# print(log(10))
# print(ceil(10.5))

# import calendar
# # print(calendar.month(2026, 3))
# print(calendar.calendar(2026))
# print(calendar.isleap(2026))

# User-defined modules
import example

# example.sum(10,20)
# example.subtract(10,20)
# example.multiplication(10,20)
# print(example.x)

# External modules
# import numpy as np
# print(np.pi)