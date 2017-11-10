import numpy as np


class Kernel(object):
    def __init__(self, *args):
        self.sigmas = args

    def __call__(self, t, t_dash):
        exponential = (np.exp(self.sigmas[0])) * (np.exp(-0.5 * np.exp(self.sigmas[1]) * ((t - t_dash)**2)))
        return exponential
