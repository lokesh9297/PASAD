import numpy as np

def find_eig(data):
    eigenValues, eigenVectors = np.linalg.eig(np.dot(data, data.T))
    idx = eigenValues.argsort()[::-1]
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]
    return eigenValues, eigenVectors