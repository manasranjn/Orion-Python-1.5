# WAP to check largest of three numbers

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b and a > c:
#     print("Largest number is: ", a)
# elif b > a and b > c:
#     print("Largest number is: ", b)
# else:   
#     print("Largest number is: ", c)


# WAP to find sum of first n natural numbers

# n = int(input("Enter a number: "))
# sum = 0

# for i in range(1, n+1):
#     sum += i

# print("Sum of first ", n, " natural numbers is: ", sum)

# WAP to count numbers of ditigits in a number

# num = int(input("Enter a number: "))
# count = 0

# while num> 0:
#     num //= 10
#     count += 1

# print("Number of digits in the number is: ", count)

# WAP to reverse a number

# num = int(input("Enter a number: "))
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10

# print("Reverse of the number is: ", reverse)

# WAP to check whether a number is palindrome or not
# WAP to check wheather a year is leap year or not
# WAP to count even and odd numbers in a list
# WAP to print multiplication table of a number
# WAP to find factorial of a number
# WAP to print numbers from 1 to n

s = "           Hello everyone, welcome to Python programming!"
print(len(s))
print(s[3])
print(s[-3])
print(s[0:4])
print(s[3:])
print(s[:7])
print(s[:])
print(s[-6:-1])

# Inbuilt methods of string
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.split())
print(s.split('o'))
l = s.split()
print(l)
print(" ".join(l))
print(s)
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace('o', 'aaaaaaaaa'))
print(s.find('o'))
print(s.find('k'))
print(s.find('o', 20))
print(s.rfind('o'))
print(s.rfind('o', 30))
print(s.index('o'))
print(s.count('o'))
print(s.startswith("  "))
print(s.endswith("ng!"))
print('abcd'.isalpha())
print('abcd'.isalnum())
print('1234a'.isdigit())