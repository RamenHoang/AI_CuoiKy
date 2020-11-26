import numpy as np
import pandas as pd

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def d_sigmoid(z):
    s = sigmoid(z)
    return s*(1-s)


def add_bias(a):
    return np.insert(a, 0, 1, axis=1)


def feedforward(x):
    z = []
    a = [add_bias(x)]
    for i in range(1, nL):
        z_i = np.dot(a[i-1], w[i-1].T)
        a_i = sigmoid(z_i)
        if i < nL - 1:
            a_i = add_bias(a_i)
        z.append(z_i)
        a.append(a_i)
    # print('f')
    return z, a


def backprop(x, y):
    w_grad = [np.zeros(_w.shape) for _w in w]
    z, a = feedforward(x)

    # loss = 1.0 * (y^ - y) ** 2 / 2
    d_a = 2*(a[-1] - y)

    r = None
    for l in range(1, nL):
        i = -l
        d_z = d_sigmoid(z[i])
        if i < -1:
            r = np.dot(r, w[i + 1][:,1:])*d_z
        if i == -1:
            r = d_a * d_z
        w_grad[i] = np.dot(a[i - 1].T, r)
        # print('l')

    # print('b')
    return w_grad


def predict(x):
    z, a = feedforward(x)
    return z, a


if __name__ == '__main__':
    df = pd.read_csv('Advertising.csv')
    m_d, n_d = df.values.shape

    # Chuẩn hoá [0..1]
    df = (df - df.min())/(df.max() - df.min())

    print('Data and label:')
    print(df.values)

    inputs = (df.values[:m_d - 10, 0:n_d - 1])
    outputs = (df.values[:m_d - 10, n_d-1:n_d])

    Xtest = (df.values[m_d - 10:m_d, 0:n_d - 1])
    Ytest = (df.values[m_d - 10:m_d, n_d-1:n_d])

    layers = [n_d-1, 3, 4, 1]
    print(layers)
    nL = len(layers)

    loop = 10000
    eta = 0.002
    w = [np.random.randn(l2, l1+1) for l2, l1 in zip(layers[1:], layers[:-1])]
    
    # Train
    while loop > 0:
        w_grad = backprop(inputs, outputs)
        w = [W - eta*W_grad.T for W, W_grad in zip(w, w_grad)]
        loop -= 1

    # init weights

    print('Final weights: \n', w)

    print('Evaluate:')
    for i in range(10):
        z, a = predict(np.array([Xtest[i]]))
        print('Predict:', a[-1], ' ---- result: ', Ytest[i][0])