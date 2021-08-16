# accessing elements from a dictionary
new_dict = {1:"Hello", 2:"hi", 3:"Hey"}
print(new_dict)
print(new_dict[1])
print(new_dict.get(3))
# updating value
new_dict[1] = "namaste"
print(new_dict)
# adding value
new_dict[4] = "walla"
print(new_dict)

# creating a new dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares)
# remove a particular item
print(squares.pop(4))
# remove an orbitary item
print(squares.popitem())
# delete a particular item
del squares[2]
print(squares)

