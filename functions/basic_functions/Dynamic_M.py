import numpy as np
from scipy.linalg import pinv

def dynamic_M(robot, q, **kwargs):
    opt = {
        'axes': ['T', 'all', 'R'],
        'dof': []
    }
    opt.update(kwargs)

    if not opt['dof']:
        axes = opt['axes']
        if axes == 'T':
            dof = [1, 1, 1, 0, 0, 0]
        elif axes == 'R':
            dof = [0, 0, 0, 1, 1, 1]
        elif axes == 'all':
            dof = [1, 1, 1, 1, 1, 1]
    else:
        dof = opt['dof']

    dof = np.array(dof, dtype=bool)
    J = robot.jacob0(q)

    if np.linalg.matrix_rank(J) < 6:
        print('Robot is in degenerate configuration')
        m = 0
        return m

    Ji = pinv(J)
    M = robot.inertia(q)
    Mx = Ji.T @ M @ Ji
    Mx = Mx[np.ix_(dof, dof)]
    e = np.linalg.eigvals(Mx)
    m = np.min(e) / np.max(e)

    return m
