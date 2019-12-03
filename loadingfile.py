# loading  file with standard python library

import csv
import numpy
from matplotlib import pyplot
from pathlib import Path
from numpy import loadtxt
from pandas import read_csv
from pandas import set_option
from pandas.plotting import scatter_matrix

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
print("data shape")
print(dataPandas.shape)

# print  first 20 rows of data
print()
print("peek at data")
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
print('class count')
print(class_count)
print()
# correlations
print('data correlation based on pearson distribution')
correlations = dataPandas.corr(method='pearson')
print(correlations)
print()
# data skew
print('data skew')
skew = dataPandas.skew()
print(skew)

# plot  histograms
hist = dataPandas.hist()
pyplot.show()

# plot univariate plot
dataPandas.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)
pyplot.show()

# plot box plot
dataPandas.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
pyplot.show()


# correlation plot
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(ticks)
ax.set_yticklabels(ticks)
pyplot.show()

# scatter  matrix
scatter_matrix(dataPandas)
pyplot.show()
