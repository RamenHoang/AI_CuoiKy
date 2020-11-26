import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ex2data1.csv')

m, n = df.values.shape

# Tạo tập train
X_train = df.values[:m-10, 0:n-1]
y_train = df.values[:m-10, n-1:n]
X_train = np.insert(X_train, 0, values=1, axis=1)
# Tạo tập test
X_test = df.values[m-10:, 0:n-1]
y_test = df.values[m-10:, n-1:n]
X_test = np.insert(X_test, 0, values=1, axis=1)

plt.scatter(df.values[:,0], df.values[:,1],s=50)
plt.show()

# Chuyển các đầu ra có giá trị 0 -> -1
for i in range(m-10):
    if (y_train[i,0] == 0):
        y_train[i,0] = -1
for i in range(10):
    if (y_test[i,0] == 0):
        y_test[i,0] = -1

# Hàm dự đoán: sign(X*w)
def pred(X, w):
    return np.sign(np.dot(X, w))

# Hàm tính trượt dốc của Perceptron
# Loss = -y*sign(X*w) ~ -y*X*w
# d(w)(Loss) = -y*X
def perceptron(X, y, w, loop):
    N = X.shape[1]
    d = X.shape[0]
    for iters in range(loop):
        mix_id = np.random.permutation(d)
        for i in range(d):
            xi = X[mix_id[i], :].reshape(1, N)
            yi = y[mix_id[i], 0:1]

            _y = pred(xi, w)[0]
            if _y != yi:
                m = 0.0002*yi*xi
                w = w + m.T
    return w


w = np.random.randn(n, 1)
loop = 10000

w = perceptron(X_train, y_train, w, loop)

print('Final weights: \n', w)

print('Evaluate:')
for i in range(10):
    print('Predict:', pred(X_test[i], w)[0], ' ---- result: ', y_test[i][0])
