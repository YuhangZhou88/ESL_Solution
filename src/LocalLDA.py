import numpy as np
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.base import BaseEstimator
from sklearn.utils.multiclass import unique_labels


def _class_weighted_means(x0, X, y, gamma):
    """Compute class weighted means .

    Parameters
    ----------
    x0: a local point

    X : array-like of shape (n_samples, n_features)
        Input data.

    y : array-like of shape (n_samples,) or (n_samples, n_targets)
        Target values.

    gamma: float, exp(-gamma * (x-y)^2)

    Returns
    -------
    means : array-like of shape (n_classes, n_features)
        Class weighted means.
    """
    classes, y = np.unique(y, return_inverse=True)
    cnt = np.bincount(y)
    x0 = x0.reshape(1, -1)
    weights = rbf_kernel(X, Y=x0, gamma=gamma)
    W = np.diag(weights.ravel())
    X_new = np.dot(W, X)
    means = np.zeros(shape=(len(classes), X_new.shape[1]))
    np.add.at(means, y, X_new)
    means /= cnt[:, None]
    return means


def _class_cov(x0, X, y, gamma):
    """Compute weighted within-class covariance matrix.

    The per-class covariance are weighted by the class priors.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input data.

    y : array-like of shape (n_samples,) or (n_samples, n_targets)
        Target values.

    Returns
    -------
    cov : array-like of shape (n_features, n_features)
        Weighted within-class covariance matrix
    """
    classes = np.unique(y)
    cov = np.zeros(shape=(X.shape[1], X.shape[1]))
    N = X.shape[0]
    K = len(classes)
    if N <= K:
        raise ValueError('number of samples must be greater than number of classes')
    for idx, group in enumerate(classes):
        Xg = X[y == group, :]
        Xg -= _class_weighted_means(x0, X, y, gamma=gamma)[idx]
        cov += np.dot(Xg.T, Xg)
    return cov / (N - K)


class LocalLinearDiscriminantAnalysis(BaseEstimator):

    def __init__(self, gamma=0.5):
        """

        Parameters
        ----------
        gamma
        """
        self.gamma = gamma

    def predict(self, x0, X, y):
        """

        Parameters
        ----------
        x0
        X
        y

        Returns
        -------

        """
        X, y = self._validate_data(X, y, ensure_min_samples=2, estimator=self,
                                   dtype=[np.float64, np.float32])
        self.classes_ = unique_labels(y)
        n_samples, _ = X.shape
        n_classes = len(self.classes_)

        if n_samples <= n_classes:
            raise ValueError("The number of samples must be more "
                             "than the number of classes.")

        cov = _class_cov(x0, X, y, self.gamma)
        cov_inv = np.linalg.inv(cov)
        means = _class_weighted_means(x0, X, y, self.gamma)

        deltas = []
        for i in range(n_classes):
            delta = np.dot(x0.T, np.dot(cov_inv, means[i]))
            delta += -0.5 * np.dot(means[i].T, np.dot(cov_inv, means[i]))
            _, y_ = np.unique(y, return_inverse=True)
            cnt = np.bincount(y_)
            pi = cnt[i]/n_samples
            delta += np.log(pi)
            deltas.append(delta)

        deltas = np.asarray(deltas)
        y_pred = self.classes_.take(deltas.argmax())
        return y_pred
