'''
try to test the function Generate_Joint
'''

from basic_Matlab_to_Python.functions.basic_functions.Generate_Joint import generate_joint
from basic_Matlab_to_Python.functions.basic_functions.BuildOneRobot import BuildOneRobot
from basic_Matlab_to_Python.functions.extend_functions.global_one_robot import global_one_robot
Parameters = {
    'Couple': 0,
    'Joint_Limit': 0,
    'Monte_Carlo': 0,
    'Iteration': 0,
    'Joint_Num': 15,
    'Precision': 0.02,
    'Error': 0.0001,
    'Indice': ["Manipulability", "Inverse Condition Number", "Minimum Singular Value", "Order-Independent Manipulability"]
}
robot_type = 'Cylindrical'
Flag=0
Robot,N_Dof = BuildOneRobot(robot_type)
num=15
qs,count=generate_joint(Robot,0,JointNum=num, Path=robot_type)
Dex, V_Robot, Global_Indices =global_one_robot(Flag, Robot, robot_type, Parameters, 'g')
