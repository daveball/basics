# feature selection recursive example Logistic regression
from pathlib import Path
from numpy import set_printoptions
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
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

model = LogisticRegression(solver='liblinear')
rfe = RFE(model, 3)
fit = rfe.fit(x, y)
set_printoptions(precision=3)
print("Number of features %d" % fit.n_features_)
print("Selected features %s" % fit.support_)
print("Feature Ranking %s" % fit.ranking_)
