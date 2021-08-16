# creating an empty tuple
tuple1 = ()
print(tuple1)

# creating tuples with integer elements
tuple2 = (1, 2, 3)
print(tuple2)

# tuple with mixed datatypes
tuple3 = (101, "Anirban", 2000.00, "Hr Dept")
print(tuple3)

# creation of nested tuples
tuple4 = ("points", [1,4,5], (7,5,6))
print(tuple4)

# tuple can be created without any paranthesis
# alaso called tuple packing
# tuple5 = 101, "aadada", 20000, "Hr Dept"
# print(tuple5)

# # tuple unpacking is also possible
# empid,empname,empdept = tuple5
# print(empid)
# print(empname)
# print(empdept)
# print(type(tuple5))

# accessing elements in a tuple
tuple1 = ('w', 'e', '1', 'c', 'o')
print(tuple1[1])
print(tuple1[2])
#  nested tuple

nest_tuple2 = ("point", [1,2,3], (8,7,4))
print(nest_tuple2)
print(nest_tuple2[0][2])
print(nest_tuple2[1][2])

# slicing tuple contents
tuple1 = 'w', '2', 'e', 't', 'y', '3'
print(tuple1[1:2])
print(tuple1[:-3])
print(tuple1[:])

# tuple elements which are immutable
tuple1 = 'w', '2', 'e', 't', 'y', '3'
print(tuple1)
# tupes can be reassigned
tuple1 = 'a', '3', 'e', 'g', 'h', '2'
print(tuple1)

# concatinating of tuple
tuple1 = 'w', '2', 'e'
tuple2 = 't', 'y', '3'
print(tuple1 + tuple2)
print(("again",) * 5)

# deletion operatin on tuple
tuple12 = 'w', '2', 'e', 't', 'y', '3'
# del tuple12[2]

# immutable elements cannot be deleted in tuple
# but entire tuple can be deleted
del tuple12
# print(tuple12)

# tuple methods
tuple5 = 'w', '2', 'e', 't', 'y', '3', 'e'
print(tuple5.count('e'))
print(tuple5.index('w'))   

# tuple operations
tuple4 = 'w', '2', 'e', 't', 'y', '3'
print("e" in tuple4)
print("w" not in tuple4)
print("a" not in tuple4)

# iteration in tuples
tuple8 = 'w', '2', 'e', 't', 'y', '3'
for letters in tuple8:
    print("letter is :",letters)

    # built-in functions with tuples
tuple7 = 22,23,565,55,56,67,778
print(max(tuple7))
print(min(tuple7))
print(sorted(tuple7))
print(len(tuple7))


