import numpy as np
import plotly.graph_objects as go
from numpy.linalg import inv
from scipy.stats import chi2

n = 10
sigma = np.sqrt(0.5)

# prepare data
ones = np.ones(n)
x = np.random.uniform(0, 1, n)
x = np.sort(x)
x_square = np.square(x)
x_cubic = np.power(x, 3)

X = np.column_stack((ones, x, x_square, x_cubic))
X_T = X.transpose()

epsilon = np.random.normal(0, sigma, n)

beta = np.array([1, 1, 2, 3])
y_theory = X @ beta
y_realized = y_theory + epsilon

beta_hat = inv(X_T @ X) @ X_T @ y_realized
y_estimated = X @ beta_hat

# method 1
var_beta_hat = inv(X_T @ X) * (sigma**2)
tmp = X @ var_beta_hat
tmp = tmp @ X_T
width = np.diag(tmp)
width = np.sqrt(width)
width_upper = y_estimated + 1.96 * width
width_lower = y_estimated - 1.96 * width


# method 2
U_T = np.linalg.cholesky(X_T @ X)
U = U_T.transpose()
U_inv = inv(U)

p = 0.95
df = 4
num = 100

region_arr = []

for i in range(num):
    a = np.random.normal(0, 1, df)
    a = U_inv @ a
    a_norm = np.linalg.norm(a, ord=2)

    r = sigma * np.sqrt(chi2.ppf(p, df))
    a = a * (r/a_norm)

    beta2 = beta + a
    region = np.dot(X, beta2)
    region_arr.append(region)

# plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y_estimated, mode='lines+markers', name='estimated', line_color='#0066ff'))
fig.add_trace(go.Scatter(x=x, y=width_upper, mode='lines+markers', name='upper1', line_color='#009933'))
fig.add_trace(go.Scatter(x=x, y=width_lower, mode='lines+markers', name='lower1', line_color='#009933'))

for i in range(num):
    fig.add_trace(go.Scatter(x=x, y=region_arr[i], mode='lines', line_color='#cc3300'))

fig.show()
