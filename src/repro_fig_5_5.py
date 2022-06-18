import pathlib
import numpy as np
import pandas as pd
from patsy import dmatrix
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# phoneme data
data = pd.read_csv(DATA_PATH.joinpath("phoneme.csv"), header=0)
values = ['aa', 'ao']
data = data.loc[data['g'].isin(values)]


X = pd.DataFrame(data.iloc[:, 1:257])
y = pd.DataFrame(data['g'])
frequencies = np.arange(257)[1:]
H = dmatrix('cr(x, df=11)', {'x': frequencies}, return_type="dataframe")

X_ast = np.dot(X, H)
clf = LogisticRegression(random_state=0).fit(X_ast, y)
beta = clf.coef_
red_curve = np.dot(H, beta.transpose())
red_curve = np.array(red_curve).ravel()

X = np.array(X)
clf = LogisticRegression(random_state=0).fit(X, y)
beta = clf.coef_
raw = np.array(beta).ravel()

fig = go.Figure()

fig.add_trace(go.Scatter(x=frequencies, y=red_curve, mode='lines', name='Regularized', line_color='#cc3300'))
fig.add_trace(go.Scatter(x=frequencies, y=raw, mode='lines', name='Raw', line_color='#666699'))

# Add figure title
fig.update_layout(
    title_text='Phoneme Classification: Raw and Restricted Logistic Regression'
)
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="center",
    x=0.5
))

# Set x-axis title
fig.update_xaxes(title_text='Frequency')

# Set y-axes titles
fig.update_yaxes(title_text='Logistic Regression Coefficients')

fig.show()