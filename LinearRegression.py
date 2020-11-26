import numpy as np
import pandas as pd
# from matplotlib import py_trainplot
df = pd.read_csv('Advertising.csv')

df = (df - df.mean())/df.std()

# Tạo tập train
m, n = df.values.shape
X_train = df.values[:m-10, 0:n-1]
y_train = df.values[:m-10, n-1:n]
X_train = np.insert(X_train, 0, values=1, axis=1)

# Tạo tập test
X_test = df.values[m-10:, 0:n-1]
y_test = df.values[m-10:, n-1:n]
X_test = np.insert(X_test, 0, values=1, axis=1)

# Hàm dự đoán: ^y = X*w X[m,n], w[n,1]
def pred(X_train, w):
    return np.dot(X_train, w)

# Hàm tính loss mean square 
def computeLoss(X_train, y_train, w):
    diff = np.power((pred(X_train, w) - y_train), 2)
    loss = (1.0/(2 * len(X_train))) * np.sum(diff)
    return loss


# Hàm tính trượt dốc
# d(w)(Loss) = d(w)(1/2m * (X*w - y)^2) = 1/m * X.T * (X*w - y)
def gradient_descent(X_train, y_train, w, alpha, loop):
    m = len(y_train)
    for i in range(loop):
        dLoss = np.dot(X_train.T, np.dot(X_train, w) - y_train) / m
        # print(computeLoss(X_train, y_train, w))
        w -= alpha * dLoss
        miX_train_id = np.random.permutation(m)
        X_train = X_train[miX_train_id]
        y_train = y_train[miX_train_id]
    return w

w = np.zeros((X_train.shape[1], 1))

alpha = 0.003
loop = 1000

w = gradient_descent(X_train, y_train, w, alpha, loop)

print('Final weights: \n', w)

print('Evaluate:')
for i in range(10):
    print('Predict:', pred(X_test[i], w)[0], ' ---- result: ', y_test[i][0])
