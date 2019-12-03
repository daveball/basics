# feature selection k fold cross example Logistic regression
from pathlib import Path


from sklearn.model_selection import LeaveOneOut
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
num_fold = 10

leaveOneOut = LeaveOneOut()
model = LogisticRegression(solver="liblinear")
result = cross_val_score(model, x, y, cv=leaveOneOut)
print("Accuracy of  result %.3f%% (%.3f%%)" % (result.mean()*100, result.std()*100))
