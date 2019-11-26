# pandas basics
import numpy
import pandas


# series one D array
myArray = numpy.array([1, 2, 3])
rowNames = ['a', 'b', 'c']
mySeries = pandas.Series(myArray, index=rowNames)
print(mySeries)

# multidimensional array
myArrayMulti = numpy.array([[1, 2, 3], [4, 5, 6]])
rowNames2 = ['a', 'b']
colNames2 = ['one', 'two', 'three']
myDataFrame = pandas.DataFrame(myArrayMulti, index=rowNames2, columns=colNames2)
print(myDataFrame)

# print first column
print(myDataFrame.two)
