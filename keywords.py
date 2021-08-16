# and, or , not
print(True and True)
print(True or False)
print(not True)

def a_void_function():
    a = 1
    b = 2
    c =a + b
    return(c)
x = a_void_function()
print(x)

# def
def function_name(parameters):
    pass
function_name(10)

# del
a = 10
print(a)
del a 
print(a)

# if elif, esle
num = 2
if num == 1:
    print('One')
elif num == 2:  
    print('two')
else:
    print('Something else')

    # try, raise, catch, finally
try:
    x = 9
#     raise ZeroDivisionError
except ZeroDivisonError:
    print("Division cannot be done")
finally:
    print("Execution successful")

    # for
for i in range(1, 10+1):
    print(i)


# from import
import math
from math import cos
print(cos(45))

# in
a = [1, 2, 3, 5]
print(4 in a)
print(4 not in a)
print(2 in a)


# is
print(True is True)

# lambda
a = lambda x: x*2
for i in range(1,6):
    print(i,a(i))

    # return
def func_return():
    a = 10
    return a 
print(func_return())

# while
# i = 5
# while(i>0):
#     print(i)
#     i-=1

    # with
with open('example.txt', 'w') as my_file:
    my_file.write("Hello World")

    