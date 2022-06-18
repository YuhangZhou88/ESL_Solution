import pandas as pd
import numpy as np
import pathlib
from sklearn.metrics import mean_squared_error
from GraphicalGaussian import GraphicalGaussian, GraphicalGaussianEM

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# data
X = pd.read_csv(DATA_PATH.joinpath("cytometry_data.csv"), header=0)
X = np.asarray(X)
"""
Gamma: represents network in Figure 17.1
       X1 - X11 are in the following order
       Raf, Mek, Plcg, PIP2, PIP3, Erk, Akt, PKA, PKC, P38, Jnk
        -0.55 & 0.36 & 0 & 0 & 0 & 0 & -0.0048 & 0.00046 & 0 & -6.5 & 0
       if two nodes i, j are connected, Gamma[i][j] = 0, else Gamma[i][j] = 1 
"""
Gamma = pd.read_csv(DATA_PATH.joinpath("cytometry_gamma.csv"), header=0)
Gamma = np.asarray(Gamma)

# set first 1000 Jnk as NaN
X_jnk = X.copy()
X_jnk[np.arange(1000), -1] = np.nan

model_EM = GraphicalGaussianEM()
model_EM.fit(X_jnk, Gamma)
cov_EM = model_EM.covariance_
est_X = model_EM.imputed_X

est_values, true_values = est_X[np.arange(1000), -1], X[np.arange(1000), -1]
print('Estimated mean is {} vs actual mean is {}'.format(np.mean(est_values), np.mean(true_values)))
print('MSE is {}'.format(mean_squared_error(est_values, true_values)))


# drop missing value
X_drop = X.copy()
X_drop = X[1000:, :]

model = GraphicalGaussian(verbose=True)
S = np.cov(X_drop, rowvar=False)
model.fit(S, Gamma)

print('The norm of the difference between to estimated covariance matrix is {}'
      .format(np.linalg.norm(model.covariance_ - cov_EM)))
