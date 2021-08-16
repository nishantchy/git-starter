# defining and declaring and array
arr= [10, 20, 30, 40, 50]
print(arr)

# accessing array elements
print(arr[0])
print(arr[1])
print(arr[-2])

brands = ["coke", "Apple", "microsoft", "toyota"]
print(brands)

# finding the lenght of arrray
num_brands = len(brands)
print(num_brands)

# adding an elemnt to an array
brands.append("Intel")
print(brands)

# removing the elements froam an array
colors = ["violet", "red", "blue", "yellow", "white", "black"]
del colors[3]
print(colors)

colors.remove("blue")
print(colors)


colors.pop(2)
print(colors)

# modifying elements of an array using indexing
fruits = ["mango", "apple", "banana", "pineapple", "guava"]
print(fruits)
fruits[1] = "orange"
print(fruits)

fruits[-1] = "cherry"
print(fruits)
fruits.append("kera")
print(fruits)

# concatinating the array using + operator
concat = [1, 2, 3]
concat + [4, 5, 6]
print(concat)
concat = concat + [4, 5, 6]
print(concat)

# repeating elements in an array
repeat = ["a"]
repeat = repeat * 5
print(repeat)

# slicing elements in an array
fruits = ["Apple", "banana", "grapes", "guava", "orange"]
print(fruits)
print(fruits[1:4])
print(fruits[:2])
print(fruits[-4:])
print(fruits[-3:-2])

# defining and declaring multidimensional array
multd = [1,2],[3,4],[5,6],[7,8]
print(multd)
print(multd[:2])
print(multd[2][1])
print(multd[3][0])