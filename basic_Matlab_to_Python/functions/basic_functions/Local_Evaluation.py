'''
这里边就是提到的进行local evaluation 的计算，里面有论文里提到的indics 这种引用方法可以进行借鉴
'''
import numpy as np


def local_evaluation(Index, N_DoF, Y, m, M, R):
    Results = 0
    U, S, V = np.linalg.svd(Y)
    hmmi = np.sqrt(1 / np.trace(np.linalg.pinv(Y @ Y.T)))
    SS = np.diag(S)
    J = Y[:3, :]
    Sum_Singular = np.sqrt(np.linalg.det(J @ J.T))

    H = Y @ M
    U, DS, V = np.linalg.svd(H)
    Dynamic_SS = np.diag(DS)
    Dynamic_Sum_Singular = np.sqrt(np.linalg.det(H @ H.T))
    Dynamic_hmmi = np.sqrt(1 / np.trace(np.linalg.pinv(H @ H.T)))

    if Index == 'Manipulability':
        Results = Sum_Singular * R
    elif Index == 'Inverse Condition Number':
        Results = np.min(SS) / np.max(SS) * R
    elif Index == 'Minimum Singular Value':
        Results = np.min(SS) * R
    elif Index == 'Order-Independent Manipulability':
        Results = Sum_Singular ** (1 / N_DoF)
    elif Index == 'Harmonic Mean Manipulability Index':
        Results = hmmi * R
    elif Index == 'Isotropic Index':
        Results = (Sum_Singular ** (1 / N_DoF)) / np.mean(SS) * R
    elif Index == 'Condition number':
        Results = np.max(SS) / np.min(SS) * R
    elif Index == 'Max Singular':
        Results = np.max(SS) * R
    elif Index == 'Dynamic Manipulability':
        Results = m * R
        Results = Dynamic_Sum_Singular * R
    elif Index == 'Dynamic Inverse Condition Number':
        Results = np.min(Dynamic_SS) / np.max(Dynamic_SS) * R
    elif Index == 'Dynamic Minimum Singular Value':
        Results = np.min(Dynamic_SS) * R
    elif Index == 'Dynamic Order-Independent Manipulability':
        Results = Dynamic_Sum_Singular ** (1 / N_DoF)
    elif Index == 'Dynamic Harmonic Mean Manipulability Index':
        Results = Dynamic_hmmi * R
    elif Index == 'Dynamic Isotropic Index':
        Results = (Dynamic_Sum_Singular ** (1 / N_DoF)) / np.mean(Dynamic_SS) * R
    elif Index == 'Dynamic Condition Number':
        Results = np.max(Dynamic_SS) / np.min(Dynamic_SS) * R
    elif Index == 'Dynamic Max Singular':
        Results = np.max(Dynamic_SS) * R

    return Results
