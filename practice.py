# set
# subject = {
#     "phy", "che", "mat", "c", "phy", "mat",
#     "oop", "c"
# }

# print(subject)
# print(len(subject))

# dictionary
marks = {}

x = int(input("Enter phy number : "))
marks.update({"phy" : x})
x = int(input("Enter mat number : "))
marks.update({"mat" : x})
x = int(input("Enter che number : "))
marks.update({"che" : x})

print(marks)