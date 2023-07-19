import numpy as np


def joint_limitation(qPtr, qUp, qDown, N):
    Qjoint = np.array(qPtr)
    QLimUp = np.array(qUp)
    QLimDown = np.array(qDown)

    p = 1

    for i in range(N):
        t = (QLimUp[i] - QLimDown[i]) * (QLimUp[i] - QLimDown[i])
        T1 = Qjoint[i] - QLimDown[i]
        T2 = QLimUp[i] - Qjoint[i]
        p = p * T1 * T2 / t * 5

    R = 1 - np.exp(-p)

    return R
