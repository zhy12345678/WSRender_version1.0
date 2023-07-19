import numpy as np

def rt2tr(R, t):
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = t
    return T
