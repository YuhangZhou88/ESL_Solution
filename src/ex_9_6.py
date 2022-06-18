import pathlib
import numpy as np
import pandas as pd
import prim
from pyearth import Earth
from pygam import LinearGAM, s
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# ozone data
data = pd.read_csv(DATA_PATH.joinpath("ozone.csv"), header=0)
X = data.loc[:, 'radiation':'wind']
y = pd.DataFrame(data.loc[:, 'ozone'])
y['ozone'] = np.power((y['ozone']), 1 / 3)

# fit GAM
reg_gam = LinearGAM(s(0) + s(1) + s(2)).fit(X, y)
# reg_gam.summary()
y_pred_gam = reg_gam.predict(X)
print('MSE for GAM is {:.2f}'.format(mean_squared_error(y_pred_gam, y)))

# fit tree
reg_tree = DecisionTreeRegressor(max_leaf_nodes=5)
reg_tree.fit(X, y)
y_pred_tree = reg_tree.predict(X)
print('MSE for tree is {:.2f}'.format(mean_squared_error(y_pred_tree, y)))

# fit MARS
reg_mars = Earth()
reg_mars.fit(X, y)
# print(reg_mars.summary())
y_pred_mars = reg_mars.predict(X)
print('MSE for MARS is {:.2f}'.format(mean_squared_error(y_pred_mars, y)))

# plot 4 * 4
data_plot = X
data_plot['y'] = y
data_plot['y_pred_gam'] = y_pred_gam
data_plot['y_pred_mars'] = y_pred_mars
data_plot['y_pred_tree'] = y_pred_tree

data_pct = data_plot
data_pct = data_pct.sort_values('radiation')
data_pct = data_pct[data_pct['wind'] < data_pct['wind'].quantile(0.75)]
data_pct = data_pct[data_pct['temperature'] < data_pct['temperature'].quantile(0.75)]

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=data_pct['radiation'], y=data_pct['y'],
                         mode='markers',
                         marker=dict(
                                    color='LightSkyBlue',
                                    size=20
                                ),
                         name='raw'))

fig.add_trace(go.Scatter(x=data_pct['radiation'], y=data_pct['y_pred_gam'],
                         mode='lines',
                         name='GAM'))


fig.add_trace(go.Scatter(x=data_pct['radiation'], y=data_pct['y_pred_tree'],
                         mode='lines',
                         name='Tree'))


fig.add_trace(go.Scatter(x=data_pct['radiation'], y=data_pct['y_pred_mars'],
                         mode='lines',
                         name='MARS'))

fig.update_layout(
    xaxis_title="radiation",
    yaxis_title="Cubic Root Ozone",
)

fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="center",
    x=0.5
))
fig.show()