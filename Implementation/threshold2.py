import numpy as np
from scipy.linalg import hankel

def find_threshold_part3(X_train, X_theta, U, centroid, L):

    Xtrain = hankel(X_train[:L], X_train[L-1:])
    
    UT = U.T
    pXtrain = np.matmul(UT, Xtrain)
    
    cov_matrix = np.cov(pXtrain, rowvar=True)
    
    inv_cov_matrix = np.linalg.inv(cov_matrix)
    
    dtrain_matrix = centroid - pXtrain
    dtrain_scores = np.sqrt(np.einsum('ij,ij->j', np.dot(inv_cov_matrix, dtrain_matrix), dtrain_matrix))
    
    Xtheta = hankel(X_theta[:L], X_theta[L-1:])
    pXtheta = np.matmul(UT, Xtheta)
    
    dtest_matrix = centroid - pXtheta
    dtest_scores = np.sqrt(np.einsum('ij,ij->j', np.dot(inv_cov_matrix, dtest_matrix), dtest_matrix))
    
    dtest_theta = np.max(dtest_scores)
    
    return dtest_theta, dtrain_scores, dtest_scores, inv_cov_matrix
