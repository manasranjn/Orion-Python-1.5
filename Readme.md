# What is Programming ?

## Complier

## Interpreter

# Types of Programming Languages

1. Low Level Language- Assembly Language, Machine Code
2. High Level Language-

# What is Python ?

Guido van Rossum in 1991

## Features of Python-

## What is Syntax?

Print()

# Comments

1. Single Line Comment- #
2. Multi Line Comment- """ """/''' '''

# Variable

first_name

# Data Type-

## Number Types-

1. int -
2. float -
3. complex -

## Sequence Types-

1. String - s = "hello"
2. List - l1 = [1,2,3,4,5]
3. Tupple - t1 = (1,2,3,4,5,6)

## Mapping Types-

1. Dictionary -
   student = {
   'name': "Smith",
   'age': 20,
   'marks': [50,60,70]
   }

## Boolean Type-

1. Boolean - True/False

## Set Type-

1. Set - s1 = {1,1,1,2,2,3,3,4,4,5,5,6,78}

## None Type-

x = None

type()

##Operators  
Operators are the symbols or keywords used to perform  
Operations on variables and value or operands.
eg : a+b, a-b, a/b, a*b
here a and b are operands and '+,-,/,*' are the operators

1. Arithmetic Operators:- used for mathematical operations with numeric values.
   +:Addition
   -:Subtraction
   /:Division
   \*:Multiplication
   %:Modulus(Remainder)
   \*\*:Power or exponent
   //:Floor division(Round Value)

2. Assignment Operators:- Used to assign value to variables.
   = : Assigns value to variable
   += : Adds and Assigns value to the left operand -= : Subtract and assign value to the left operand
   \*= : Multiply and assign value to the left operand
   /= : Divide and assign value to the left operand
   //=: Flloor divide and assign value to the left operand
   %= : Modulus and assign value to the left operand
   \*\*=: Powers and assign value to the left operand

3. Comparison Operator(Relational):- Used to Compare value and it returns only two values either true or false.
   == (Equals to) -> returns True if both the operandds are same
   != (Not Equals to) -> Returns True if both the operands are not same

   > (Greater than) -> Returns True if left side operand is greater than right operand
   > <(Less than) -> Returns True if right operand is greater than left operands
   > =(Greater than equal to) :-> It returns true if left operand is greater or same as right operand
   > <=(Less than equal to) -> It returns true if left opernad is less or same as right operand
   > 4.Logical Operator: Used for logical AND, OR, NOT operation
   > AND -> Returs true if both the operands are true, else false
   > OR -> Returns true if any the operand are true , if both are false then returns false
   > NOT -> Returns the Oppostive Value

4. Membership Operator:- Used to check if a value or variable is found im a sequence or not.
   in -> Returns True if value found in the sequence.
   not in -> Returns true if value not found in the sequence

5. Identity Operator: Checks Whether Two objects share the same memory location.
   is -> Returns True if Operand refer to same object.
   is not -> Returns True if operand refer to different object

# Conditional Statements

It is a statement that controls the flow of a program by executing certain code blocks only if specific condition are satisfied.
With these statements we can make decisions in our codes that's why it is also known as decision making statements.

##Types of Conditional Statements:
1.If statements : If only executes the block if the condition is true
Syntax: if condition:
instructions
if the condition is false nothing happens

2.If-Else Statements: It executes if block only when the condition is true otherwise the else block will executes. When we
have two sets of instructions but one condition and we want to execute only one block of code in that situation we can use if
else statements.
Syntax: if condition:
instructions
else:
Instructions

3.elif Statements : It is used to check multiple conditions in a sequence , the first condition that's true will get executed if
none are true then else block will execute.
It is used for several cases handling.
Syntax: if condition:
instructions
elif condition:
instructions
elif condition:
instructions
else:
Instructions

# Loops- To repeat something

## for loop-

1)for i in range(statIndex, endIndex, Steps):
instruction
2)for i in sequence:
instruction

## while loop-

initialization
while condition:
instruction

# Nested Loop

for i in range():
for j in range():
instruction

## Loop Controls-

break - It is used to stop the loop immediately
continue - Is is used to skip current iteration value
pass - It does nothing, used as a placeholder

# Property of String and It's inbuilt methods

- A string is a sequence of characters used to represent text.
- Strings are enclosed in single quote, double quote or triple quote.

## Properties:

- Strings are index base collection where each and every character can be accessed by their individual index which starts from Zero.
- Strings can’t be changed after creation because strings are immutable in nature. Any operations that modify a string returns a new string
- String Supports Slicing -> s[1:6]
- Strings are case Sensitive, where a and A are different characters.
- Strings supports concatenation and repetition

- Note: Use 'len' method to find length.
  S[5:] - It returns a substring up to last characters.
  s[:5] - It reruns a substring from starting index (0th index).
  eg: s= "Hello"
  print(s[-2]) //l

## Inbuilt methods

Lower():- It returns a string in a lower case. eg: print(s.lower())
Upper():- It returns a string in upper case. eg: print(s.upper())
Capitalize():- It returns a string with first letter capital. eg: print(s.capitalize())
title() :- It Converts the first character of each word to uppercase. eg: print(s.title())
Split() :- It splits a string into lists buy a specified separator. eg: print(s.split(" "))
join() :- It joins elements of iterable with string. eg: print(" " .join(s))
replace() :- It replace a substring with a new string. It accepts two arguments. Search Value and new Value. eg: print(s.replace('a','aa'))
strip() :- It removes the starting and ending whitespaces. eg: print(s.strip())
lstrip() :- It removes the starting whitespaces only. eg: print(s.lstrip())
rstrip() :- It removes the ending whitespaces only. eg: print(s.rstrip())
find() :- It returns the first occurrence index of a substring. eg: print(s.find('o'))
rfind() :- It returns the last occurrence index of a substring . eg: print(s.rfind())
index() :- It returns the index number of a substring if found, if not found then returns a ValueError. eg: print(s.index('o'))
isalpha() :- It checks if all the characters are alphabetic , it returns the value in Boolean.eg: print(s.isalpha())
isdigit() :- It checks all the characters are digits or not , it returns value in Boolean . eg: print(s.isdigit())
isalnum() :- It checks if all characters are alpha numeric or not, it returns value in Boolean. eg: print(s.isalnum())
isdecimal() :- It checks if the value is decimal or not, it returns value in Boolean. eg: print(s.isdecimal())
count() :- It counts total occurrence of a substring. eg: print(s.count('l'))
startswith() :- It checks if the string starts with a substring , it returns value in Boolean. eg: print(s.startswith('h'))
endswith() :- It checks if the string end with a substring, it returns value in Boolean. eg: print(s.endswith())

# Dictionary

a dictionary is a mutable and unordered collection of key value pairs.
Each key must be unique.
dictionary can store any type of values.
Dictionary are denoted by {}

## Characteristic of Dictionary:

1. Key value pair - Data is stored as pairs by using single colon. e.g: key:value.
2. Unordered - Items are not stored in a sequence and the order may change.
3. Mutable - Dictionary can be modified after created.
4. No Duplicate key - No key should be duplicate, duplicate key will override the previous value.
   -> To create a dictionary either we use curly braces {} or we can use dict() constructor.
   e.g: example = dict(key = value, key= value)
   -Also we can create an empty dictionary.
   e.g: my_dict = {}
   Operations on Dictionary:-
5. To add a new key :-
   dictionaryName['keyName'] = Value
6. To edit a key:-
   dictionaryName['keyName'] = Value
7. To delete an key :-
   del dictionaryName['keyname']
8. To iterate through a dictionary :-
   (a). for key,value in dictionaryName.items():
   print(key,value)
   (b). for key in dictionaryName:
   print(key)

## Dictionary Inbuilt Methods:

1. Copy():- It returns a copy of the original dictionary.
   dictionaryName.copy()
2. Keys() :- It returns all the key available in a dictionary.
   dictionaryName.keys()
3. Values() :- It return a list of all the values available in a dictionary.
   dictionaryName.values()
4. items() :- It returns view of key-value pairs from a dictionary .
   dictionaryName.items()
5. get() :- It returns value of the key or a default value.

- It accepts two arguments, a> Searchkey, b> Default-Value
- If the key is present in the dictionary then it will return the value else then it will return the default value.
  dictionaryName.get("keyName", defaultValue)

6. pop() :- It removes key and returns it's value.
   dictionaryName.get("keyName")
7. popitem() :- It removes the last key.
   dictioanryName.popitem()
8. update() :- It is used to update a keys value.
   dictionaryName.update({"key":value})
9. clear() :- It removes all the items from a dictionary.
   dictionaryName.clear()
