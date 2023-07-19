import numpy as np
from spatialmath.base.transforms3d import trotx, troty, trotz, transl
from basic_Matlab_to_Python.functions.basic_functions.rt2tr import rt2tr
import matplotlib.pyplot as plt

def PlaceTwoRobot(RightRobot, LeftRobot, Num, *args, **kwargs):
    deg = np.pi / 180
    AxisMax=0
    opt = {'visual': ['Teach', 'On', 'Bimanual', 'Off', 'Human', 'HumanReal'],
           'baseright': [],
           'baseleft': [],
           'Range': [],
           'range': ['Big', 'Small']}

    opt.update(kwargs)
    Robot = RightRobot

    if 'baseright' in opt and opt['baseright']:
        BaseRight = opt['baseright']
    else:
        BaseRight = np.zeros(6)
    RightRobot.base= trotx(BaseRight[3]) * troty(BaseRight[4]) * trotz(BaseRight[5])
    R = RightRobot.base.R
    t = BaseRight[:3]

    RightRobot.base = rt2tr(R, t)


    if 'baseleft' not in opt or opt['baseleft'] is None:
        BaseLeft = np.zeros(6)
    else:
        BaseLeft = opt['baseleft']
    LeftRobot.base = trotx(BaseLeft[3]) * troty(BaseLeft[4]) * trotz(BaseLeft[5])
    R = LeftRobot.base.R
    t = BaseLeft[:3]
    LeftRobot.base = rt2tr(R, t)


    if 'Range' in opt and opt['Range']:
        WS_Range = opt['Range']
    else:
        if 'range' in opt and opt['range'] == 'Big':
            Size=0.5#这边的Size不是很对
            AxisMax = Size * 2
        elif 'range' in opt and opt['range']=='Small':
            Size=4
            AxisMax = Size * 1.2

        WS_Range = [-AxisMax, AxisMax, -AxisMax, AxisMax, -AxisMax, AxisMax]

    visual_type = opt['visual']

    if visual_type == 'HumanReal':
        RightRobot.plotopt = {'workspace': WS_Range}
        RightRobot.name = 'RightRobot'
        RightRobot.base = transl(BaseRight[:3]) * trotx(BaseRight[3]) * troty(BaseRight[4]) * trotz(BaseRight[5])

        LeftRobot.plotopt = {'workspace': WS_Range}
        LeftRobot.name = 'LeftRobot'
        LeftRobot.base = transl(BaseLeft[:3]) * trotx(BaseLeft[3]) * troty(BaseLeft[4]) * trotz(BaseLeft[5])

    elif visual_type == 'Human':
        RightRobot.plotopt = {'workspace': WS_Range}
        RightRobot.name = 'RightRobot'
        RightRobot.base = transl(BaseRight[:3]) * trotx(BaseRight[3]) * troty(BaseRight[4]) * trotz(BaseRight[5])

        LeftRobot.plotopt = {'workspace': WS_Range}
        LeftRobot.name = 'LeftRobot'
        LeftRobot.base = transl(BaseLeft[:3]) * trotx(BaseLeft[3]) * troty(BaseLeft[4]) * trotz(BaseLeft[5])

        qsL = [0 * deg, 0 * deg, 0, np.pi / 2, 0]
        LeftRobot.name = 'LeftArm'
        LeftRobot.plot(qsL, 'nowrist', 'noname', 'shading', 'noshadow', 'nobase', 'jointcolor', 'g', 'tile1color',
                       [1, 1, 1])
        plt.hold(True)

        qsR = [0 * deg, 0 * deg, 0, np.pi / 2, 0]
        RightRobot.name = 'RightArm'
        RightRobot.plot(qsR, 'nowrist', 'noname', 'shading', 'noshadow', 'nobase', 'jointcolor', 'g', 'tile1color',
                        [1, 1, 1])
        plt.hold(True)

    elif visual_type == 'Teach':
        Robot.plotopt = {'workspace': WS_Range}
        Robot.teach()

    elif visual_type == 'Bimanual':
        RightRobot.plotopt = {'workspace': WS_Range * 2}
        RightRobot.name = f'RightRobot{Num}'
        LeftRobot.plotopt = {'workspace': WS_Range * 2}
        LeftRobot.name = f'LeftRobot{Num}'

        Q = RightRobot.qlim
        N_DoF = Q.shape[1]
        qs = np.zeros((1, N_DoF))

        for i in range(N_DoF):
            qs[0, i] = (Q[i, 1] + Q[i, 0]) / 2

        RightRobot.plot(qs, 'noname', 'noshadow', 'nobase', 'tile1color', [1, 1, 1])
        plt.hold(True)

        Q = LeftRobot.qlim
        N_DoF = Q.shape[1]
        qs = np.zeros((1, N_DoF))

        for i in range(N_DoF):
            qs[0, i] = (Q[i, 1] + Q[i, 0]) / 2

        LeftRobot.plot(qs, 'noname', 'noshadow', 'nobase', 'tile1color', [1, 1, 1])
        plt.hold(True)

    elif visual_type == 'Off':
        out = 'No visualization'

    plt.show()

    return  RightRobot,LeftRobot
