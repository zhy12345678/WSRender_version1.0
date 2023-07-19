import numpy as np
from scipy.spatial.transform import Rotation as R
from spatialmath.base.transforms3d import trotx, troty, trotz, transl

def PlaceRobot(RightRobot, Size, *args, **kwargs):
    deg = np.pi / 180
    N_DoF, _ = RightRobot.qlim.shape

    opt = {'visual': ['Off', 'Teach', 'On'], 'base': [], 'Range': [], 'range': ['Big', 'Small']}
    opt.update(kwargs)

    Robot = RightRobot
    if not opt['base']:
        Base = np.zeros(6)
    else:
        Base = opt['base']

    Robot.base = transl(Base[:3]) * trotx(Base[3]) * troty(Base[4]) * trotz(Base[5])

    if not opt['Range']:
        if opt['range'] == 'Big':
            AxisMax = Size * 1.5 + (Base[0] + Base[1] + Base[2]) / 3
            WS_Range = [-AxisMax, AxisMax, -AxisMax, AxisMax, -AxisMax, AxisMax]
        elif opt['range'] == 'Small':
            AxisMax = Size * 1.2
            WS_Range = [-AxisMax, AxisMax, -AxisMax, AxisMax, -AxisMax, AxisMax]
    else:
        WS_Range = opt['Range']

    Robot.plotopt = {'workspace': WS_Range}

    if opt['visual'] == 'Teach':
        Robot.teach()
        out = 'Teach'
    elif opt['visual'] == 'On':
        Q = Robot.qlim
        qs = np.zeros(N_DoF)
        for i in range(N_DoF):
            qs[i] = (Q[i, 1] + Q[i, 0]) / 2

        Robot.plot(qs, options={'noshadow': True, 'jointcolor': 'r', 'tile1color': [1, 1, 1], 'nowrist': True})
        out = 'On'
    else:
        out = 'No visualization'

    return out
