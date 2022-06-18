import pathlib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# get original data
train = np.genfromtxt(DATA_PATH.joinpath("zip_train_2and3.csv"), dtype=float, delimiter=',', skip_header=True)
test = np.genfromtxt(DATA_PATH.joinpath("zip_test_2and3.csv"), dtype=float, delimiter=',', skip_header=True)

# prepare training and testing data
x_train, y_train = train[:, 1:], train[:, 0]
x_test, y_test = test[:, 1:], test[:, 0]

# for classification purpose
# we assign 1 to digit '3' and 0 to '2'
y_train[y_train == 3] = 1
y_train[y_train == 2] = 0
y_test[y_test == 3] = 1
y_test[y_test == 2] = 0


# a utility function to assign prediction
def assign(arr):
    arr[arr >= 0.5] = 1
    arr[arr < 0.5] = 0


# a utility function to calculate error rate
# of predictions
def getErrorRate(a, b):
    if a.size != b.size:
        raise ValueError('Expect input arrays have equal size, a has {}, b has {}'.
                        format(a.size, b.size))

    if a.size == 0:
        raise ValueError('Expect non-empty input arrays')

    return np.sum(a != b) / a.size


# Linear Regression
reg = LinearRegression().fit(x_train, y_train)
pred_test = reg.predict(x_test)
assign(pred_test)
print('Test error rate of Linear Regression is {:.2%}'
    .format(getErrorRate(pred_test, y_test)))


pred_train = reg.predict(x_train)
assign(pred_train)
print('Train error rate of Linear Regression is {:.2%}'
    .format(getErrorRate(pred_train, y_train)))


# run separate K-NN classifiers
for k in range(1, 16):
    # fit the model
    neigh = KNeighborsClassifier(n_neighbors=k)
    neigh.fit(x_train, y_train)

    # test error
    pred_knn_test = neigh.predict(x_test)
    assign(pred_knn_test)
    test_error_rate = getErrorRate(pred_knn_test, y_test)
    # train error
    pred_knn_train = neigh.predict(x_train)
    assign(pred_knn_train)
    train_error_rate = getErrorRate(pred_knn_train, y_train)

    print('k-NN Model: k is {}, train/test error rates are {:.2%} and {:.2%}'
        .format(k, train_error_rate, test_error_rate))