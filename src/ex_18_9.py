import numpy as np
from sklearn import svm
from sklearn.datasets import make_blobs

# we create 40 separable points
n_samples_raw = 400
X_raw, y_raw, centers = make_blobs(n_samples=n_samples_raw,
                                   n_features=1000,
                                   centers=2,
                                   random_state=2,
                                   return_centers=True)
y_raw[y_raw == 0] = -1
c0 = centers[0]
c1 = centers[1]
dist = np.linalg.norm(c0 - c1)

n_samples = 20
indices, indices_1 = [], []
r0, r1 = 0, 0
for i in range(n_samples_raw):
    if y_raw[i] == -1:
        cur_dist = np.linalg.norm(X_raw[i] - c0)
        if cur_dist < dist / 3 and len(indices) < n_samples:
            indices.append(i)
            r0 = max(r0, cur_dist)
    else:
        cur_dist_1 = np.linalg.norm(X_raw[i] - c1)
        if cur_dist_1 < dist / 3 and len(indices_1) < n_samples:
            indices_1.append(i)
            r1 = max(r1, cur_dist_1)

X = X_raw[indices + indices_1]
y = y_raw[indices + indices_1]


clf = svm.SVC(kernel='linear', C=1000)
clf.fit(X, y)

margin_svm = 2 / np.linalg.norm(clf.coef_)

U, D, V_T = np.linalg.svd(X, full_matrices=False)
D = np.diag(D)
V = V_T.T

beta = V @ np.linalg.inv(D) @ U.T @ y

margin_data_piling = 2 / np.linalg.norm(beta)

print('Margins from optimal hyperplane (SVM) and data piling are {} and {}, respectively.'
      .format(margin_svm, margin_data_piling))
