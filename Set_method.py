collection = set() 
collection.add(1)
collection.add(12)
collection.add(13)
collection.add(15)
collection.add("Ashraf")
collection.add("Bin")
collection.add((3,5,1,9)) # touple

# collection.remove(15)
print(collection)
print(len(collection))

# collection.clear()
# print(collection)
# print(len(collection))

print(collection.pop())

collection2 = {11, 23, 12, 15}
print(collection.intersection(collection2))
print(collection.union(collection2))