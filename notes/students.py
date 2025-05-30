students = {
    "1": {
        "firstname": "Alice",
        "lastname": "Smith",
        "age": 20
    },
    "2": {
        "firstname": "Bob",
        "lastname": "Johnson",
        "age": 22
    },
    "3": {
        "firstname": "Charlie",
        "lastname": "Lee",
        "age": 32
    },
    "4": {
        "firstname": "Kenneth",
        "lastname": "LeeMon",
        "age": 23
    },
    "5": {
        "firstname": "Steve",
        "lastname": "Crux",
        "age": 14
    },
    "6": {
        "firstname": "John",
        "lastname": "Grefiel",
        "age": 25
    },
    "7": {
        "firstname": "Diana",
        "lastname": "Garcia",
        "age": 21
    },
    "8": {
        "firstname": "Emily",
        "lastname": "Stone",
        "age": 18
    },
    "9": {
        "firstname": "Michael",
        "lastname": "Jordan",
        "age": 19
    },
    "10": {
        "firstname": "Nathan",
        "lastname": "Drake",
        "age": 24
    }
}


selectStudents = input("Please select students : ")
print(students.get(selectStudents, "Student is not exists"))
# print(students.keys())
# print(students.values())

# removeStudents = input("Please select to remove students : ")
# print(students.pop(selectStudents, "Student is not exists"))
if selectStudents in students:
    print("exist")
else :
    print("not exist")