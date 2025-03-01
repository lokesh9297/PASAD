import numpy as np

def project_onto_signal_subspace(data, eigenVectors, r):
    U, sigma, V = np.linalg.svd(data)
    V = V.T

    X_elem = np.array([sigma[i] * np.outer(U[:, i], V[:, i]) for i in range(0, r)])
    X_train_extracted = X_elem.sum(axis=0)
    X_train_extracted_data = np.asarray(list(X_train_extracted[:, 0]) + list(X_train_extracted[:, -1]))

    U = eigenVectors[:, :r]
    UT = U.T
    pX = np.matmul(UT, X_train_extracted)
    centroid = np.mean(pX, axis=1)
    centroid = centroid[:, np.newaxis]

    return centroid, pX, U, X_train_extracted_data
