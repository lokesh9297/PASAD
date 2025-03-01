import numpy as np

def create_embedding(data):
    N = len(data)
    L = N // 2
    k = N - L + 1
    trajectory_matrix = np.zeros((L,k))
    c = 0
    for i in range(L):
        d = c
        for j in range(k):
            trajectory_matrix[i][j] = data[d]
            d = d + 1
        c = c + 1
    
    return trajectory_matrix, L