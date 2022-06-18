import pathlib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()


# a utility function to calculate error rate
# of predictions
def getErrorRate(a, b):
    return np.sum(a != b) / a.size


data = pd.read_csv(DATA_PATH.joinpath("spam.csv"), header=0)
X = data.iloc[:, :-1]
y = data.iloc[:, -1:]

p = 58
m_values = np.arange(1, np.sqrt(p), dtype=int)
oob_list = []
testError_list = []
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
y_train = y_train.to_numpy().flatten()
y_test = y_test.to_numpy().flatten()

for m in m_values:
    print('running for m: {}'.format(m))
    clf = RandomForestClassifier(random_state=42, n_estimators=2500, oob_score=True, max_features=m)
    clf.fit(X_train, y_train)
    oob_list.append(1-clf.oob_score_)
    print('oob is: {}'.format(1-clf.oob_score_))
    y_predict = clf.predict(X_test)
    error_rate = getErrorRate(y_predict, y_test)
    testError_list.append(error_rate)
    print('error rate is: {}'.format(error_rate))

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=m_values, y=oob_list,
                         mode='lines',
                         name='OOB Error'))

fig.add_trace(go.Scatter(x=m_values, y=testError_list,
                         mode='lines',
                         name='Test Error'))

fig.update_layout(
    xaxis_title="m",
    yaxis_title="Error Rate",
)

fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="center",
    x=0.5
))
fig.show()