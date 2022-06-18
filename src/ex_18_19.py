import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.stats.multitest as mt
import pathlib
import timeit

# get relative data folder
PATH = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = PATH.joinpath("data").resolve()

# data
X = pd.read_csv(DATA_PATH.joinpath("microarray.csv"), header=0)


def t_wrapper(arr, ind1=None, ind2=None):
    s1 = np.asarray(arr[ind1])
    s2 = np.asarray(arr[ind2])
    return stats.ttest_ind(s1, s2).statistic


def perm_t_wrapper(arr, perms):
    res = []
    for perm in perms:
        ind1 = perm[:44]
        ind2 = perm[44:]
        t = t_wrapper(arr, ind1=ind1, ind2=ind2)
        res.append(t)
    return res


def get_t_stats(X, ind1, ind2):
    res = X.apply(t_wrapper, axis=1, ind1=ind1, ind2=ind2)
    return np.asarray(res)


def get_tjk(X, K=1000):
    perms = []
    for _ in range(K):
        perms.append(np.random.permutation(58))
    res = X.apply(perm_t_wrapper, axis=1, perms=perms)
    return res


def get_FDR(t_orig, tjk, C, K):
    R_obs = (abs(t_orig) > C).sum()
    E_V = (abs(tjk) > C).sum() / K
    FDR = E_V / R_obs
    return FDR


def get_p_value(t_orig, tjk):
    p, K = tjk.shape
    p_values = np.arange(p)
    for p_ in range(p):
        p_values[p_] = np.count_nonzero(tjk[p_] > t_orig[p_]) / K
    p_values.sort()
    return p_values


normal_indices = np.arange(44)
sensitive_indices = np.arange(44, 58)
t_orig = get_t_stats(X, normal_indices, sensitive_indices)

tjk = get_tjk(X, K=1000)  # ~ 20mins
C = [4, 4.101, 4.2]
plugin_FDR = []
for c in C:
    plugin_FDR.append(get_FDR(t_orig, np.asarray(tjk), c))

p_values = get_p_value(t_orig, np.asarray(tjk))

alphas = plugin_FDR
L = []
for alpha in alphas:
    res = mt.multipletests(p_values, alpha, is_sorted=True)
    L.append(np.count_nonzero(res.reject))

print(L)
