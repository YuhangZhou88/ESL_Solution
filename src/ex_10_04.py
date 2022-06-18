import numpy as np
from sklearn.ensemble import AdaBoostClassifier
import plotly.graph_objects as go


p = 10
mean = np.zeros(p)
cov = np.identity(p)


def classify(X):
    if np.linalg.norm(X) > np.sqrt(9.34):
        return 1
    else:
        return -1


n_train = 1000
X_train = np.random.multivariate_normal(mean, cov, n_train)
y_train = np.apply_along_axis(classify, 1, X_train)


n_test = 10000
X_test = np.random.multivariate_normal(mean, cov, n_test)
y_test = np.apply_along_axis(classify, 1, X_test)

num_iterations = 800
test_errors = []
train_errors = []
for i in range(num_iterations):
    i += 800
    clf = AdaBoostClassifier(n_estimators=i+1, random_state=0)
    clf.fit(X_train, y_train)
    train_error = 1 - clf.score(X_train, y_train)
    train_errors.append(train_error)
    test_error = 1 - clf.score(X_test, y_test)
    test_errors.append(test_error)
    print('Num. of Iteration is {}, Train Error is:{}, Test Error is: {}'.format(i+1, train_error, test_error))

# Create traces
fig = go.Figure()

fig.add_trace(go.Scatter(x=np.arange(num_iterations), y=np.asarray(train_errors),
                         mode='lines',
                         name='Train error'))

fig.add_trace(go.Scatter(x=np.arange(num_iterations), y=np.asarray(test_errors),
                         mode='lines',
                         name='Test error'))

fig.update_layout(
    xaxis_title="Boosting Iterations",
    yaxis_title="Train and Test Error",
)

fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="center",
    x=0.5
))

fig.show()