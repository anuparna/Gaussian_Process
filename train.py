import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF


def covariance(kernel, frames, sigma2):
    k_list = []
    for time1 in frames:
        for time2 in frames:
            k_list.append(kernel(time1, time2))
    return np.reshape(k_list, (len(frames), len(frames)))


def train(gp, kernel, frames, coordinates, sigma2):
    K = covariance(kernel, frames, sigma2)
    print(K)
    kernel = RBF(10, (1e-3, 1e4))
    if gp:
        gp.fit(np.reshape(frames, (-1, 1)), coordinates)
    else:
        gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
    return gp


def test(gp, new_frames):
    #print((np.reshape(frames,(-1,1))).shape)
    y_pred, mse = gp.predict(np.reshape(new_frames,(-1,1)), return_std=True)
    return y_pred, mse

