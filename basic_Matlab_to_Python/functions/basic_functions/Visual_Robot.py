import numpy as np
from roboticstoolbox import Robot
from spatialmath import SE3
from spatialmath.base import transl


def visual_robot(right_robot,left_robot,size,**kwargs):
    deg=np.pi/180
    opt_visual=['Teach','On','Bimanual','Off','Human','HumanReal']
    opt_range=['Big','Small']
    opt={
        'visual':'Teach',
        'Range':'None',
        'range':'Big'
    }
    BaseRight = np.array([0.1, 0.2, 0.3, 0, 0, 0])
    BaseLeft = np.array([0.2, 0.3, 0.4, 0, 0, 0])

    opt.update(kwargs)
    robot=right_robot

    if opt['Range'] is None:
        if opt['range'] == 'Big':
            axis_max=size*2
            WS_Range=[-axis_max,axis_max,-axis_max,axis_max,-axis_max,axis_max]
        elif opt['range']=='Small':
            axis_max=size*1.2
            WS_Range=[-axis_max,axis_max,-axis_max,axis_max,-axis_max,axis_max]
        else:
            WS_Range=opt['Range']

    if opt['visual'] == 'HumanReal' or opt['visual'] == 'Human':
        right_robot.plotopt = {'workspace': WS_Range}
        right_robot.name = 'RightRobot'
        right_robot.base = SE3(transl(BaseRight[0:3])) * SE3.trotx(BaseRight[3]) * SE3.troty(BaseRight[4]) * SE3.trotz(
            BaseRight[5])

        left_robot.plotopt = {'workspace': WS_Range}
        left_robot.name = 'LeftRobot'
        left_robot.base = SE3(transl(BaseLeft[0:3])) * SE3.trotx(BaseLeft[3]) * SE3.troty(BaseLeft[4]) * SE3.trotz(
            BaseLeft[5])



