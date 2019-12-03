# feature selection recursive example Logistic regression
from pathlib import Path


from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from pandas import read_csv

# load  data  file
data_folder = Path("data/")
file_to_open = data_folder / "pima-indians-diabetes.csv"

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataFrame = read_csv(file_to_open, names=names)
array = dataFrame.values

# data
x = array[:, 0:8]
y = array[:, 8]

# set up test data
num_split = 10
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits=num_split,  test_size=test_size, random_state=seed)
model = LogisticRegression(solver="liblinear")

result = cross_val_score(model, x, y, cv=kfold)
print("Accuracy of  result %.3f%% (%.3f%%)" % (result.mean()*100, result.std()*100))
