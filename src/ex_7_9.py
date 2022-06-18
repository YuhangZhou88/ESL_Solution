import pathlib
import numpy as np
import itertools
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn import linear_model


# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

data = pd.read_csv(DATA_PATH.joinpath("prostate.csv"), header=0)
data_train = data.loc[data['train'] == 'T']
data_test = data.loc[data['train'] == 'F']

X_train = data_train.loc[:, 'lcavol':'pgg45']
X_test = data_test.loc[:, 'lcavol':'pgg45']
y_train = pd.DataFrame(data_train.loc[:, 'lpsa'])
y_test = pd.DataFrame(data_test.loc[:, 'lpsa'])


# model = OLS(y_train, X_train)
# res = model.fit()
# print(res.summary())

def get_fitted_model(X, y):
    lr = linear_model.LinearRegression(normalize=True)
    lr.fit(X, y)
    return lr


def get_err_and_sigma(X, y, fitted_model):
    N = X.shape[0]
    p = X.shape[1]
    expected_err = mean_squared_error(y, fitted_model.predict(X))  # (7.17) in ESL
    est_sigma_square = N * expected_err / (N - p - 1)  # below (3.8) in ESL
    return [N, p, expected_err, est_sigma_square]


def get_AIC(X, y, fitted_model):
    [N, p, expected_err, est_sigma_square] = get_err_and_sigma(X, y, fitted_model)
    return expected_err + 2 * p * est_sigma_square/N  # (7.30) in ESL


def get_BIC(X, y, fitted_model):
    [N, p, expected_err, est_sigma_square] = get_err_and_sigma(X, y, fitted_model)
    return N/est_sigma_square * (expected_err + np.log(N) * p * est_sigma_square/N)  # (7.36) in ESL


def get_CV(X, y, fitted_model, cv=10):
    res = cross_val_score(fitted_model, X, y, scoring='neg_mean_squared_error', cv=cv)
    return -1 * max(res)


# TODO: implement .632 bootstrap
def get_bootstrap(X, y, fitted_model):
    return 1

#
# def get_min(a, b):
#     if a is None and b is not None:
#         return b
#     if a is not None and b is None:
#         return a
#     return min(a, b)


def run_best_subset(X, y):
    num_features = X.shape[1]
    num_feature_list = []
    features_list = []
    AIC_list = []
    BIC_list = []
    CV5_list = []
    CV10_list = []
    bootstrap_list = []
    for k in range(num_features):
        k += 1
        print(k)

        for comb in itertools.combinations(X.columns, k):
            X_selected = X[list(comb)]
            fitted_model = get_fitted_model(X_selected, y)

            num_feature_list.append(k)
            features_list.append(comb)

            AIC_list.append(get_AIC(X_selected, y, fitted_model))
            BIC_list.append(get_BIC(X_selected, y, fitted_model))
            CV5_list.append(get_CV(X_selected, y, fitted_model, cv=5))
            CV10_list.append(get_CV(X_selected, y, fitted_model, cv=10))
            bootstrap_list.append(get_bootstrap(X_selected, y, fitted_model))

    df = pd.DataFrame({'num_features': num_feature_list,
                       'features': features_list,
                       'AIC': AIC_list,
                       'BIC': BIC_list,
                       '5-fold CV': CV5_list,
                       '10-fold CV': CV10_list,
                       'bootstrap': bootstrap_list})

    df_AIC = df[df.groupby('num_features')['AIC'].transform(min) == df['AIC']]

    return df


test = run_best_subset(X_train, y_train)
print(test)


