from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import pathlib
import numpy as np
import pandas as pd

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# train data
train = pd.read_csv(DATA_PATH.joinpath("vowel_train.csv"), header=0)

y_train = pd.DataFrame(train['y'])
y_train = y_train.to_numpy()
y_train = np.reshape(y_train, (1, len(y_train))).ravel()

x_train = pd.DataFrame(train[['x.1', 'x.2', 'x.3', 'x.4', 'x.5', 'x.6', 'x.7', 'x.8', 'x.9', 'x.10']])
x_train = x_train.to_numpy()

# test data
test = pd.read_csv(DATA_PATH.joinpath("vowel_test.csv"), header=0)
y_test = pd.DataFrame(test['y'])
y_test = y_test.to_numpy()
y_test = np.reshape(y_test, (1, len(y_test))).ravel()

x_test = pd.DataFrame(test[['x.1', 'x.2', 'x.3', 'x.4', 'x.5', 'x.6', 'x.7', 'x.8', 'x.9', 'x.10']])
x_test = x_test.to_numpy()


# a utility function to calculate error rate
# of predictions
def getErrorRate(a, b):
    if a.size != b.size:
        raise ValueError('Expect input arrays have equal size, a has {}, b has {}'.
                         format(a.size, b.size))

    if a.size == 0:
        raise ValueError('Expect non-empty input arrays')

    return np.sum(a != b) / a.size


# run
clf = QuadraticDiscriminantAnalysis()
clf.fit(x_train, y_train)
y_predict = clf.predict(x_test)
errorRate = getErrorRate(y_predict, y_test)

print(errorRate)
