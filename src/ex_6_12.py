import pathlib
import numpy as np
from LocalLDA import LocalLinearDiscriminantAnalysis


# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# get original data
train = np.genfromtxt(DATA_PATH.joinpath("zip_train.csv"), dtype=float, delimiter=',', skip_header=True)
test = np.genfromtxt(DATA_PATH.joinpath("zip_test.csv"), dtype=float, delimiter=',', skip_header=True)

# prepare training and testing data
x_train = train[:, 1:]
y_train = train[:, 0]
x_test = test[:, 1:]
y_test = test[:, 0]


# clf = LinearDiscriminantAnalysis()
# clf = QuadraticDiscriminantAnalysis()
# clf.fit(x_train, y_train)
# y_pred = clf.predict(x_train)
#
# err=0
# for i in range(len(y_pred)):
#     if y_pred[i] != y_train[i]:
#         err += 1
#
# print(err/len(y_pred))

clf = LocalLinearDiscriminantAnalysis(gamma=0.01)

err = 0
for i in range(x_test.shape[0]):
    print('running for {} -th point, current error rate: {}'.format(i, err / (i + 1)))
    pred = clf.predict(x_test[i], x_train, y_train)
    if pred != y_test[i]:
        err += 1

print(err / x_test.shape[0])
