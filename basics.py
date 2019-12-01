# basic data types
# integers
from typing import Dict, Union

x = 10
y = 3
s = x + y  # sum
print(s)
sub = x - y  # subtraction
print(sub)
p = x * y  # product
print(p)
d = x / y  # division
print(d)
fd = x // y  # floor division
print(fd)
m = x % y  # modulus
print(m)
e = x ** y  # exponent
print(e)
# float
z = 1.1234
print(z)

# string
name = "Dave"       # A string
print(name)
surname = 'Ball'
print(surname)
# lists
myList = ['abcd', 786, 2.23, 'john', 70.2]
tinyList = [123, 'john']

print(myList)         # Prints complete list
print(myList[0])      # Prints first element of the list
print(myList[1:3])    # Prints elements starting from 2nd till 3rd
print(myList[2:])     # Prints elements starting from 3rd element
print(tinyList * 2)   # Prints list two times
print(myList + tinyList)  # Prints concatenated lists

# Tuples
myTuple = ('abcd', 786, 2.23, 'john', 70.2)
tinyTuple = (123, 'john')

print(myTuple)           # Prints complete tuple
print(myTuple[0])        # Prints first element of the tuple
print(myTuple[1:3])      # Prints elements starting from 2nd till 3rd
print(myTuple[2:])     # Prints elements starting from 3rd element
print(tinyTuple * 2)   # Prints tuple two times
print(myTuple + tinyTuple)  # Prints concatenated tuple

# dictionaries
myDict: Dict[Union[str, int], str] = {}
myDict['one'] = "This is one"
myDict[2] = "This is two"

tinyDict = {'name': 'john', 'code': 6734, 'dept': 'sales'}


print(myDict['one'])       # Prints value for 'one' key
print(myDict[2])           # Prints value for 2 key
print(tinyDict)          # Prints complete dictionary
print(tinyDict.keys())   # Prints all the keys
print(tinyDict.values())  # Prints all the values

# sets
thisSet = {"apple", "banana", "cherry"}
print(thisSet)
thisSet.add('pear')
print(thisSet)
