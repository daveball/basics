# loading  file with standard python library

import csv
import numpy
from pathlib import Path
from numpy import loadtxt
from pandas import read_csv
from pandas import set_option
# basic import
data_folder = Path("data/")
file_to_open = data_folder / "pima-indians-diabetes.csv"
raw_data = open(file_to_open, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype(float)
print(data.shape)

# import using numpy
dataNumpy = loadtxt(file_to_open, delimiter=',')
print(dataNumpy.shape)

# loading  data using pandas
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataPandas = read_csv(file_to_open, names=names)
print(dataPandas.shape)

# print  first 20 rows of data
peek = dataPandas.head(20)
print(peek)
# print  data types
types = dataPandas.dtypes
print(types)
# descriptive stats
set_option('display.width', 100)
set_option('precision', 3)
description = dataPandas.describe()
print(description)
# group by class and print  count
class_count = dataPandas.groupby('class').size()
print(class_count)

# correlations
correlations = dataPandas.corr(method= 'pearson')
print(correlations)
