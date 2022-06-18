import pandas as pd
import numpy as np
import pathlib
from sklearn.covariance import GraphicalLassoCV

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# get data
X = pd.read_csv(DATA_PATH.joinpath("cytometry_data.csv"), header=0)
nodes = list(X.columns)
X = X.to_numpy(dtype=float)

res = GraphicalLassoCV(cv=10, alphas=36).fit(X)
Sigma = res.covariance_
Theta = np.linalg.inv(Sigma)
