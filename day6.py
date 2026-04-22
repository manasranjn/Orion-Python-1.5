# Properties of Dictionary and its methods

student = {
    "name": "John",
    "age": 25,
    "courses": ["Math", "CompSci"],
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "state": "MA"
    },
}
# print(student)
# print(student['address']['city'])

person = dict(name="Alice", age=30, city="New York", marks=[85, 90, 92])
# print(person)
# print(person["name"])
# print(person["marks"])
# print(person["marks"][1])

# marks = person["marks"]
# print(marks[0])
# print(person['marks'][1])

# print(student["name"])
student['marks']= [85, 90, 92]
# print(student['marks'])
# print(student)
# student['age'] = 26
# print(student)
# del student['age']
# print(student)

# for i in student:
#     print(i)
#     print(student[i])

# Inbuilt methods of dictionary

# for a, b in student.items():
#     print(a, b)

# print(student.items())
# print(student.keys())
# print(student.values())

# s1 = student
# print(s1['name'])
# s1['name'] = 'Smith'
# print(student['name'])
# print(s1['name'])

# s2 = student.copy()
# print(s2['name'])
# s2['name'] = 'Smith'
# print(student['name'])
# print(s2['name'])

# print(student.get("name"))
# print(student.get("firstName", "Not Found"))
# student.update({"name": "Smith", "age": 26})
# print(student)
# student.pop('age')
# print(student)
# student.popitem()
# print(student)
student.clear()
print(student)