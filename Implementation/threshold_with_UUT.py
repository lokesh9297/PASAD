import numpy as np
from scipy.linalg import hankel

def find_threshold_with_UUT(X_train, X_theta, U, centroid, L):
    Xtrain = hankel(X_train[:L], X_train[L-1:])
    UT = U.T
    pXtrain = np.matmul(np.matmul(U, UT), Xtrain)
    dtrain_matrix = centroid - pXtrain
    dtrain_scores = np.linalg.norm(dtrain_matrix, axis=0, ord=2)

    Xtheta = hankel(X_theta[:L], X_theta[L-1:])
    pXtheta = np.matmul(np.matmul(U, UT), Xtheta)
    dtest_matrix = centroid - pXtheta
    dtest_scores = np.linalg.norm(dtest_matrix, axis=0, ord=2)
    dtest_theta = np.max(dtest_scores)
    return dtest_theta, dtrain_scores, dtest_scores