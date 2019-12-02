# feature selection PCA
from pathlib import Path
from numpy import set_printoptions
from sklearn.decomposition import PCA
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

pca = PCA(n_components=3)
fit = pca.fit(x)
set_printoptions(precision=3)
print("Explained variance: %s" % fit.explained_variance_ratio_)

print(fit.components_)
