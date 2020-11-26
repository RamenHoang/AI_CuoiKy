import numpy as np
from pandas import read_csv
from matplotlib import pyplot as plt

df = read_csv('ex2data1.csv')
X = df.values[:, 0:2]

k = 6

def plot_result(X, y, centers, k, title):
    for i in range(k):
        plt.scatter(X[y == i, 0],
                    X[y == i, 1],
                    s=50,
                    label='cluster ' + str(i+1))

    plt.scatter(centers[:, 0],
                centers[:, 1],
                s=250,
                marker='*',
                c='red',
                label='centroids')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# ------------------------

def init_centers(X, k):
    return X[np.random.choice(X.shape[0], k, replace=False)]

def group_data(X, centers):
    y = np.zeros(X.shape[0])

    for i in range(X.shape[0]):
        d = X[i] - centers
        d = np.linalg.norm(d, axis=1)
        y[i] = np.argmin(d)

    return y

def update_centers(X, y, k):
    centers = np.zeros((k, X.shape[1]))
    for i in range(k):
        X_i = X[y == i, :]
        centers[i] = np.mean(X_i, axis=0)

    return centers


def kmeans(X, k):
    centers = init_centers(X, k)
    y = []
    iter = 0
    while True:
        y_old = y
        y = group_data(X, centers)
        if np.array_equal(y, y_old):
            break
        centers = update_centers(X, y, k)
        iter += 1
        plot_result(X, y, centers, k, 'iter: ' + str(iter))
    
    return centers, y

centers, y = kmeans(X, k);

plot_result(X, y, centers, k, 'Final')