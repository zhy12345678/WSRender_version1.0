import numpy as np
from roboticstoolbox import Link, SerialLink
from roboticstoolbox import RevoluteMDH,RevoluteDH
from basic_Matlab_to_Python.buildRobot.DefineRobot1 import define_robot1
from basic_Matlab_to_Python.buildRobot.DefineRobot2 import define_robot2

def define_robot(index):
    if index == 1:
        Robot = define_robot1(symbolic=False)
        N_Dof = Robot.N_Dof
   # 这个自定义这里的函数还是可以进行一些改变的，可以更灵活一点
    elif index == 2:
        Robot = define_robot2(symbolic=False)
        N_Dof = Robot.N_Dof

    return N_Dof, Robot
