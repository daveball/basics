# import numpy
import matplotlib.pyplot as plt
import numpy
myList = [[1, 2, 3], [3, 4, 5]]
myArray = numpy.array(myList)
print(myArray)
# numpy array basics
print(myArray.shape)
print("First row: %s" % myArray[0])
print("Last row: %s " % myArray[1])
print("Specific row and col: %s" % myArray[0, 2])
print("Whole col: %s  " % myArray[:, 2])

# using basic maths  functions with arrays
myArray1 = numpy.array([2, 2, 2])
myArray2 = numpy.array([3, 3, 3])
print("Addition: %s" % (myArray1 + myArray2))
print("Multiplication: %s" % (myArray1 * myArray2))
print("Subtraction: %s" % (myArray1 - myArray2))
print("Division: %s" % (myArray1 / myArray2))

# plotting arrays basic
myArrayLine = numpy.array([1, 2, 3])
plt.plot(myArrayLine)
plt.xlabel(" some x axis")
plt.ylabel(" some y axis")
plt.show()

# plotting scatter graph from two arrays
myArrayScatter1 = numpy.array([1, 2, 3])
myArrayScatter2 = numpy.array([1, 2, 3])
plt.scatter(myArrayScatter1, myArrayScatter2)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

