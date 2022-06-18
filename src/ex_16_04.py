from sklearn.linear_model import Ridge, Lasso
import numpy as np

n_runs = 20
n = 50
p = 300

X = np.random.normal(size=(n, p))

n_coef = 300
beta = np.random.normal(size=(p, 1))

NSR = 0.1

sigma = np.sqrt(NSR)

eps = np.random.normal(scale=sigma, size=(p, 1))
y = X @ beta + eps


def lambda2df(lbda, X):
    p = X.shape[1]
    inv = np.linalg.inv(X.T @ X + lbda * np.identity(p))
    H = X @ inv @ X.T
    return np.trace(H)


def df2lambda(df, X):
    pass


print(1)
