# feature selection recursive example Logistic regression
from pathlib import Path


from sklearn.model_selection import train_test_split
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
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)
print("Accuracy of  result %.3f%%" % (result*100))
