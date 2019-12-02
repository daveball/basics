# data binarization
from pathlib import Path
from numpy import set_printoptions
from sklearn.preprocessing import Binarizer
from pandas import read_csv

# load  data  file
data_folder = Path("data/")
file_to_open = data_folder / "pima-indians-diabetes.csv"

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataFrame = read_csv(file_to_open, names=names)
array = dataFrame.values

# scale  data
x = array[:, 0:8]
y = array[:, 8]
binary = Binarizer(threshold=0.0).fit(x)
binarizerX = binary.fit_transform(x)

# summarise transformed data
set_printoptions(precision=3)
print(binarizerX[0:5, :])
