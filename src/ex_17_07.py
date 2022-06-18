import pandas as pd
import numpy as np
import pathlib
from GraphicalGaussian import GraphicalGaussian


# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# covariance data
S = pd.read_csv(DATA_PATH.joinpath("cytometry.csv"), header=0)
S = np.asarray(S)
"""
Gamma: represents network in Figure 17.1
       X1 - X11 are in the following order
       Raf, Mek, Plcg, PIP2, PIP3, Erk, Akt, PKA, PKC, P38, Jnk
        -0.55 & 0.36 & 0 & 0 & 0 & 0 & -0.0048 & 0.00046 & 0 & -6.5 & 0
       if two nodes i, j are connected, Gamma[i][j] = 0, else Gamma[i][j] = 1 
"""
Gamma = np.array([
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0]
], dtype=float)


# test if a matrix is symmetric
def is_symmetric(a, tol=1e-3):
    return (np.abs(a - a.T) <= tol).all()


assert is_symmetric(S)
assert is_symmetric(Gamma)

model = GraphicalGaussian(verbose=True)
cov = model.fit(S, Gamma).covariance_
theta = model.theta_



