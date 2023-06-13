'''
Input:
Robot: The robot defined using 態uildRobot� function
Output:
Length_Sum: the total length of the robot
Prismatic_Num: the number of prismatic joint
Precision: the precision for workspace discretization
Length_Sum:机器人总长度
Prismatic_Num:移动关节的个数
Precision:工作空间离散化的精度
Function:
Initial parameters for workspace visualization
Example:
[N_DoF,Robot] = BuildRobot('Articulated');
[Length_Sum,Prismatic_Num,Precision] = Initial_Precision(Robot);
'''

import numpy as np
# from spatialmath import DHRobot, roboticstoolbox as rtb
import roboticstoolbox as rtb

def initial_precision(robot):
    qlim = np.array(robot.qlim)
    length_sum = 0

    _, N_DoF = robot.config.shape
    prismatic_num = np.count_nonzero(robot.config != 'R')

    if prismatic_num == 0:
        for i in range(N_DoF):
            length_sum += robot.links[i].a + robot.links[i].d
    else:
        for i in range(N_DoF):
            length_sum += robot.links[i].a + robot.links[i].d

        for i in range(N_DoF):
            if robot.config[i] != 'R':
                P_I = i
                length_sum = qlim[P_I, 1]

    precision = length_sum / 20
    error = length_sum / 1000

    return length_sum, prismatic_num, precision, error
