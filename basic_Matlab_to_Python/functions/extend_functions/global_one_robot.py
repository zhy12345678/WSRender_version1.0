import numpy as np
import scipy.io
from roboticstoolbox import  Link, SerialLink
from basic_Matlab_to_Python.functions.basic_functions.Initial_Precision import initial_precision
from basic_Matlab_to_Python.functions.basic_functions.Generate_Joint import generate_joint
from basic_Matlab_to_Python.functions.basic_functions.reachable_ws_indices import reachable_ws_indices
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS import boundary_ws
from basic_Matlab_to_Python.functions.basic_functions.GlobalEvalution import global_evaluate


def global_one_robot(flag, robot, robot_type, parameters, evaluate='Off'):
    opt = {'evaluate': evaluate}

    num = parameters['Joint_Num']
    couple_flag = parameters['Couple']
    indice_group = parameters['Indice']
    dex=[]

    # Flag == 0: First time calculation
    # Flag == 1: Load Data


    if flag == 0:
        #length_Sum, Prismatic_Num, Precision=initial_precision(robot)
        #visual_robot(robot{2},robot{2},length_Sum,'On') 这边这个有点问题robot的用法
        qs, count = generate_joint(robot, couple_flag, JointNum=num, Path=robot_type)


        # Robot Workspace Analysis
        #reachable workplace + Local Evaluate
        #dex, path, o_volume, volume = reachable_ws_indices(robot, qs, flag, indices=indice_group, visualize=True, path=robot_type)
        dex, path= reachable_ws_indices(robot, qs, flag, indices=indice_group, visualize=True,path=robot_type)
    if flag == 1:
        # Load QS data
        filename = robot_type
        folder = 'G:\\United Kindom\\毕设\\pyqt_design\\basic_Matlab_to_Python\\'
        path_joint = folder + 'Data\\' + filename + str(num)+'.mat'
        #path_joint = os.path.join(folder, 'Data', filename + str(num) + '.mat')
        qs_data = scipy.io.loadmat(path_joint)

        # Access the 'QS' variable from the loaded data
        if 'QS' in qs_data:
            qs = qs_data['QS']
            count, _ = qs.shape
        else:
            print("Variable 'QS' not found in the loaded MATLAB file.")

        # Load Master Dex Data
        filename = robot_type
        path_dex = folder + 'Data\\' + filename + str(count) + '.mat'
        #path_dex = os.path.join(folder, 'Data', filename + str(count) + '.mat')
        dex_data = scipy.io.loadmat(path_dex)

        # Access the 'Dex' variable from the loaded data
        if 'Dex' in dex_data:
            dex = dex_data['Dex']
        else:
            print("Variable 'Dex' not found in the loaded MATLAB file.")
    # General form for Global Evaluation
    indices, global_indices = global_evaluate(dex)

    if opt['evaluate'] == 'r':
        v_robot = boundary_ws(dex, 0.1, 'r')
    elif opt['evaluate'] == 'b':
        v_robot = boundary_ws(dex, 0.1, 'b')
    elif opt['evaluate'] == 'g':
        v_robot = boundary_ws(dex, 0.1, 'g')
    else:
        v_robot = boundary_ws(dex, 0.1, 'off')

    return dex, v_robot, global_indices



# # Main script
# flag = 0
# robot = SerialLink([
#     Link([0, 0, 0, 0]),  # Joint 1
#     Link([0, 0, 0, -np.pi / 2]),  # Joint 2
#     Link([0, 0, 0, np.pi / 2]),  # Joint 3
#     Link([0.2794, 0, 0, -np.pi / 2]),  # Joint 4
#     Link([0, 0, 0, np.pi / 2]),  # Joint 5
#     Link([0.3048, 0, 0, 0])  # Joint 6
# ])
#
# parameters = {
#     'Joint_Num': 60,
#     'Couple': 1,
#     'Indice': ['Manipulability', 'Inverse ConditionNumber', 'Minimum Singular Value', 'Order-Independent Manipulability'],
# 'Precision': 0.02,
# 'Error': 0.0001
# }
#
# dex, v_robot, global_indices = global_one_robot(flag, robot, 'dVRK', parameters, evaluate='Off')
#
# import matplotlib.pyplot as plt
# fig = plt.figure(1)
# plt.scatter(dex[:, 0], dex[:, 1], c='blue')
# plt.scatter(v_robot[:, 0], v_robot[:, 1], c='red')
# plt.colorbar()
# plt.show()