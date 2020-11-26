import numpy as np
import pandas as pd

df = pd.read_csv('ex2data1.csv')
# df = (df - df.mean())/df.std()

m, n = df.values.shape
# Tạo tập train
X_train = df.values[:m-10, 0:n-1]
y_train = df.values[:m-10, n-1:n]
X_train = np.insert(X_train, 0, values=1, axis=1)
# Tạo tập test
X_test = df.values[m-10:, 0:n-1]
y_test = df.values[m-10:, n-1:n]
X_test = np.insert(X_test, 0, values=1, axis=1)

# threshold
threshold = 0.5


# hàm tính sigmoid
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


# hàm tính loss: Loss = 1/m * (y*log(sigmoid) + (1-y)*log(1-sigmoid))
def compute_cost(X, y, w):
    m = len(y)
    z = sigmoid(np.dot(X, w))
    J = np.sum(y * np.log(z) + (1 - y) * np.log(1 - z)) / m
    return J


def grad(X, y, w, alpha, loop):
    m = len(y)
    for i in range(loop):
        w = w - alpha * np.dot(X.T, sigmoid(np.dot(X, w)) - y) / m
        # print(compute_cost(X, y, w))
        mix_id = np.random.permutation(m)
        X = X[mix_id]
        y = y[mix_id]
    return w


w = np.random.randn(n, 1)
loop = 10000
alpha = 0.0002

w = grad(X_train, y_train, w, alpha, loop)

print('Final weights: \n', w)

print('Evaluate:')
for i in range(10):
    pred_v = sigmoid(np.dot(X_test[i], w))[0]
    if (pred_v > threshold):
        pred_v = 1
    else:
        pred_v = 0
    print('Predict:', pred_v, ' ---- result: ', y_test[i][0])