# data standardisation for (0 to 1)
from pathlib import Path
from typing import Any, Union

from numpy import set_printoptions
from sklearn.preprocessing import StandardScaler
from pandas import read_csv

# load  data  file
data_folder: Union[Path, Any] = Path('data/')
file_to_open = data_folder / 'pima-indians-diabetes.csv'

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataFrame = read_csv(file_to_open, names=names)
array = dataFrame.values

# scale  data
X = array[:, 0:8]
Y = array[:, 8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

# summarise transformed data
set_printoptions(precision=3)
print(rescaledX[0:5, :])
