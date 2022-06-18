import pathlib
import numpy as np
import pandas as pd
from patsy import dmatrix

from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# phoneme data
data = pd.read_csv(DATA_PATH.joinpath("phoneme.csv"), header=0)
values = ['aa', 'ao']
data = data.loc[data['g'].isin(values)]
X = data.iloc[:, 1:257]
y = pd.DataFrame(data['g'])
frequencies = np.arange(257)[1:]

# choose 5 different degree of freedoms
# internal knots are uniformly distributed by default
dfs = np.array([5, 11, 50, 100, 200])

for df in dfs:
    H = dmatrix('cr(x, df={})'.format(df), {'x': frequencies}, return_type="dataframe")
    X_ast = np.dot(X, H)
    clf = QuadraticDiscriminantAnalysis()
    acc_scores = cross_val_score(clf, X_ast, y, cv=10, scoring='accuracy') # 10 fold CV
    mean_err_rate = (1-acc_scores).mean()
    print('When df is {}, mis-classification error rate is {}'.format(df, mean_err_rate))

