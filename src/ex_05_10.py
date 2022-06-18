import numpy as np
from numpy.linalg import multi_dot
import statsmodels.api as sm
from patsy import dmatrix
import plotly.graph_objects as go
from numpy.linalg import inv


np.random.seed(42)
n = 100
sigma = 1


def f(x):
    return np.sin(12 * (x + 0.2)) / (x + 0.2)


X = np.random.uniform(0, 1, n)
X = np.sort(X)
epsilon = np.random.normal(0, sigma, n)
y_true = f(X)
y_realized = y_true + epsilon

df = 15

x_nc = dmatrix('cr(x, df={})'.format(df), {'x': X}, return_type="dataframe")
fit_natural = sm.GLM(y_realized, x_nc).fit()
line_nc = fit_natural.predict(dmatrix('cr(xp, df={})'.format(df), {'xp': X}))

H = np.asarray(x_nc)
sigma = 1
m_Sigma = sigma * sigma * (inv(np.matmul(H.transpose(), H)))
m_nc = multi_dot([H, m_Sigma, H.transpose()])
pt_var_nc = m_nc.diagonal()
pt_std_nc = np.sqrt(pt_var_nc)
upper = line_nc + 2 * pt_std_nc
lower = line_nc - 2 * pt_std_nc

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=X, y=y_realized,
                         mode='markers',
                         name='Raw'))
fig.add_trace(go.Scatter(x=X, y=y_true,
                         mode='lines',
                         name='True',
                         line_color='#993399'))
fig.add_trace(go.Scatter(x=X, y=line_nc,
                         mode='lines',
                         name='Fitted', line_color='#009933'))
fig.add_trace(go.Scatter(x=X, y=lower,
                         mode='lines',
                         name='Lower Limit', line_color='#ffff99'))
fig.add_trace(go.Scatter(x=X, y=upper,
                         mode='lines',
                         name='Upper Limit', fill='tonexty', line_color='#ffff99'))
fig.update_layout(
    xaxis_title="X",
    yaxis_title="y",
)

fig.show()
