# Operators-
## Arithmetic Operator-
a= 10
b =3
# print(a+b) # Addition
# print(a-b) # Subtraction
# print(a*b) # Multiplication
# print(a/b) # Division
# print(a//b) # Floor Division
# print(a%b) # Modulus
# print(a**b) # Exponentiation


## Assignment Operator-
a+=5  # a = a + 5|| 10 + 5 = 15
# print(a)
# a-=2
# print(a)
a*=3
# print(a)
# a/=3
# print(a)
a//=3
# print(a)
a%=2
# print(a)
a**=2
# print(a)


# Comparision Operators-
# x = 10
# y = 20
# z= 10
# print(x == y) # Equal to
# print(x != y) # Not equal to
# print(x < y) # Less than
# print(x > y) # Greater than
# print(x <= z) # Less than or equal to
# print(x >= z) # Greater than or equal to

# Logical Operators-
## and, or, not
p = True
q = False
# print(p and q) # Logical AND
# print(p and p) # Logical AND
# print(q and q) # Logical AND
# print(p or q) # Logical OR
# print(p or p) # Logical OR
# print(q or q) # Logical OR
# print(not p) # Logical NOT

# Membership Operators-
## in, not in
# l = [1,2,3,4,5]
# print(2 in l) # Membership
# print(6 in l) # Membership
# print(6 not in l) # Membership
# print(3 not in l) # Membership

# Identity Operators-
## is, is not
# x = 10
# y = 11
# z = x
# print(x is y) # Identity
# print(x is z) # Identity
# print(x is not y) # Identity


# Conditional Statements-
## if, elif, else 

# age = 2
# if age>=18:
#     print("You are an adult.")

# age = 20
# if age>=18:
#     print("You are an adult.")
# else:
#     print("You are not an adult.")

age = 60
if age < 18:
    print("You are a child.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")