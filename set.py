# we can make a list from a set
my_list = {1,2,4,5,6,7}
print(my_list)
print(type(my_list))
my_list1 = list({1,2,4,5,6,7})
print(my_list1)
print(type(my_list1))

# we can make a list from a set
my_list = {1,2,4,5,6,7}
print(my_list)
print(type(my_list))
my_list1 = list({1,2,4,5,6,7})
print(my_list1)
print(type(my_list1))

# removing and discarding elenents
my_set = {11, 21, 45, 46, 35}
print(my_set)
# discardind element not present in set, no error
my_set.discard(3)
print(my_set)
# removing element not present in set, error
# my_set.remove(2)
# print(my_set)
my_set.discard(11)
print(my_set)
my_set.remove(21)

# removing and discarding elenents
my_set = {11, 21, 45, 46, 35}
print(my_set)
# discardind element not present in set, no error
my_set.discard(3)
print(my_set)
# removing element not present in set, error
# my_set.remove(2)
# print(my_set)
my_set.discard(11)
print(my_set)
my_set.remove(21)

# using pop
my_set1 = {11, 21, 45, 46, 35}
print(my_set1)
print(my_set1.pop())
print(my_set1.pop())
my_set1.clear()
print(my_set1)

# union set
my_set1 = {11, 21, 45, 46, 35}

my_set2 = {32, 23, 55, 56, 15}
 
print(my_set1 | my_set2)
# or
print(my_set1.union(my_set2))

# intersection
my_set1 = {11, 21, 45, 46, 35}

my_set2 = {11, 21, 55, 56, 15}
print(my_set1 & my_set2)
# or
print(my_set1.intersection(my_set2))


# set difference
my_set1 = {11, 21, 45, 46, 35}

my_set2 = {32, 23, 45, 46, 15}
print(my_set1 - my_set2)
# or
print(my_set1.difference(my_set2))


# symmetric difference
my_set1 = {11, 21, 45, 46, 35}

my_set2 = {11, 23, 45, 56, 35}
print(my_set1 ^ my_set2)
# or
print(my_set1.symmetric_difference(my_set2))

# set membership
my_set1 = {11, 21, 45, 46, 35}
print(2 in my_set1)
print(2 not in my_set1)
print(11 not in my_set1)

# iterating through a set
for letter in set("welcome"):
    print(letter)

    # built-in functions in set
my_set = {1, 2, 4, 5, 6, 7, 8}
print(max(my_set))
print(min(my_set))
print(sorted(my_set))
print(len(my_set))

# frozenset
# it cannot be changed
my_set1 = frozenset([1, 2, 3, 4, 5])
my_set2 = frozenset([3, 4, 5, 6, 7])
print(my_set1)
print(my_set2)
print(my_set1.intersection(my_set2))
print(my_set2.union(my_set1))
print(my_set1 - my_set2)
print(my_set1.symmetric_difference(my_set2))
# my_set1.add(2)

