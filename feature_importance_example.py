# feature importance
from pathlib import Path

from sklearn.ensemble import ExtraTreesClassifier
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

model = ExtraTreesClassifier(n_estimators=100)
model.fit(x, y)

print(model.feature_importances_)
