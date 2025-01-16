student = {
    "name" : "Ashraf Bin Alam",
    "subject" : {
        "phy" : 90,
        "che" : 98,
        "math" : 98
    }
}
# print(len(student))

# print(student.keys())
# print(list(student.keys()))

# print(student.values())
# print(list(student.values()))
# print(student["subject"].values())

# print(student.items()) # pairs of key and value

# print(student["name2"]) # error
# print(student.get("name2")) # No Error , return None

new_dict = {
    "name2" : "Abdulllah",
    "age" : 45
}
student.update(new_dict)
print(student)