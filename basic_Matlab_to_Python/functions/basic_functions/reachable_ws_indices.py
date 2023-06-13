'''% Input:
% Robot: the robot for analysis
% QS: a list of pose
% Joint_Flag: the flag about whether to consider joint limitation or not
% opt.save = {'Save','UnSave'};
% opt.evaluate = {'On','Off'};
% opt.Indice = {}; opt.Path = [];
%
% Output:
% Dex : local indices distribution map
%
% Function:
% Calculate local indices distribution map
%
% Example:'''
import numpy as np
from roboticstoolbox import SerialLink
from basic_Matlab_to_Python.functions.basic_functions.Dynamic_M import dynamic_M
from basic_Matlab_to_Python.functions.basic_functions.local_indice_map import local_indice_map
from basic_Matlab_to_Python.functions.basic_functions.Joint_Limitation import joint_limitation
from basic_Matlab_to_Python.functions.basic_functions.Local_Evaluation import local_evaluation



def reachable_ws_indices(robot, qs, joint_flag, path='', indices=None, evaluate='Off'):
    count, _ = qs.shape
    mid_point = np.zeros((count, 3))

    # Transfer Indice Name to Array Number
    r = np.zeros(count)

    opt_save = ['Save', 'UnSave']
    opt_evaluate = ['On', 'Off']
    opt = {'save': 'UnSave', 'evaluate': 'Off', 'indice': [], 'path': ''}

    if indices is not None:
        opt['indice'] = indices

    opt['save'] = opt_save[0] if opt['save'] == 'Save' else opt_save[1]
    opt['evaluate'] = opt_evaluate[0] if opt['evaluate'] == 'On' else opt_evaluate[1]

    if path == '':
        filename = 'LocalIndice_Map'
        path = './Data/LocalIndice_Map'
    else:
        filename = path
        path = f'./Data/{filename}{count}'

    if not opt['indice']:
        num_array = np.linspace(4, 6, 3)
        cal_index = 3
    else:
        indice_group = opt['indice']
        print(indice_group)
        num_array = local_indice_map(indice_group)
        cal_index = num_array.shape[1]
        dex = np.zeros((count, cal_index))

    m = 0
    M = 0

    # Joint Limitation Information
    q = robot.qlim
    n_dof, _ = q.shape
    qupl = q[:, 1]
    qdownl = q[:, 0]

    switcher = {
        'Off': lambda x: robot.fkine(x).T,
        'On': lambda x: robot.fkine(x)
    }

    for i in range(count):
        all_t = switcher[evaluate](qs[i])

        mid_point[i, 0] = all_t[0, 3]
        mid_point[i, 1] = all_t[1, 3]
        mid_point[i, 2] = all_t[2, 3]

        if joint_flag == 1:
            r[i] = joint_limitation(qs[i], qupl, qdownl, n_dof)
        else:
            r[i] = 1

        tqs = all_t
        dex[i, 0] = tqs[0, 3]
        dex[i, 1] = tqs[1, 3]
        dex[i, 2] = tqs[2, 3]

        y = robot.jacob0(qs[i])

        for k in range(cal_index):
            evaluation = indice_group[k]

            if evaluation.startswith('Dynamic'):
                M = robot.inertia(qs[i])
                m = dynamic_M(robot, qs[i])

            dex[i, num_array[k]] = local_evaluation(evaluation, n_dof, y, m, M, r[i])

    # Normalization
    for i in range(3, cal_index):
        max_value = np.max(dex[:, i])
        dex[:, i] = dex[:, i] / max_value

    if opt['save'] == 'Save':
        np.save(path, dex)
    else:
        path = 'N'
        out = 'UnSave'

    overall_point = dex[:, 0:3]
    data = np.concatenate((overall_point, mid_point))
    _, o_volume = boundary(data)
    _, volume = boundary(overall_point)

    return dex, path, o_volume, volume









def boundary(data):
    return None, None  # Placeholder for the actual implementation


# Usage example
# n_dof, robot = create_robot()  # Assuming the robot is created using the provided create_robot() function
# qs = np.zeros((10, n_dof))  # Example joint configurations
# joint_flag = 1  # Example joint flag value
#
# reachable_ws_indices(robot, qs, joint_flag)

