import numpy as np
from sklearn.tree import DecisionTreeRegressor

np.random.seed(42)

p = 10
mean = np.zeros(p)
cov = np.identity(p)

n = 100
X = np.random.multivariate_normal(mean, cov, n)

N = 20
y = np.random.normal(0, 1, size=(n, N))
y_pred = np.copy(y)

numLeaves = 5
for i in range(N):
    y_cur = y[:, i]
    reg = DecisionTreeRegressor(max_leaf_nodes=numLeaves)
    reg.fit(X, y_cur)
    print('Depth: {}, Number of leaves:{}'.format(reg.get_depth(), reg.get_n_leaves()))
    y_pred_cur = reg.predict(X)
    y_pred[:, i] = y_pred_cur

df = 0
for i in range(y.shape[0]):
    df += np.cov(y[i, :], y_pred[i, :], ddof=0)[0][1]

print('Estimated degrees of freedom with {} terminal nodes is: {}'.format(numLeaves, df))