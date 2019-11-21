# import numpy
import numpy
myList = [[1, 2, 3], [3, 4, 5]]
myArray = numpy.array(myList)
print(myArray)
print(myArray.shape)
print("First row: %s" % myArray[0])
print("Last row: %s " % myArray[1])
print("Specific row and col: %s" % myArray[0, 2])
print("Whole col: %s  " % myArray[:, 2])

