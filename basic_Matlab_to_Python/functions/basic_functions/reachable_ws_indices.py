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
import ctypes
import os

from basic_Matlab_to_Python.functions.basic_functions.Dynamic_M import dynamic_M
from basic_Matlab_to_Python.functions.basic_functions.local_indice_map import local_indice_map
from basic_Matlab_to_Python.functions.basic_functions.Joint_Limitation import joint_limitation
from basic_Matlab_to_Python.functions.basic_functions.Local_Evaluation import local_evaluation
import numpy as np
from roboticstoolbox import ERobot
from scipy.spatial import qhull,ConvexHull


def reachable_ws_indices(Robot, QS, Joint_Flag, **kwargs):
    Count, _ = QS.shape
    Mid_Point = np.zeros((Count, 3))

    # Transfer Indice Name to Array Number
    R = np.zeros((Count, 1))


    opt = {
        'save': 'Save',
        'evaluate': 'On',
        #'volume':['Common','Operating'],
        'indices': None,
        'path': None
    }
    opt.update(kwargs)

    print(opt['indices'])

    if opt['path'] is None:
        filename = 'LocalIndice_Map'
        path = '../Data_Dex/LocalIndice_Map'
    else:
        filename = opt['path']
        path = f"./Data_Dex/{filename}{Count}"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if opt['indices'] is None:
        Num_Array = np.linspace(4, 6, 3)
        Cal_Index = 3
        Dex = np.array([[0.0] * Cal_Index for _ in range(Count)])
    else:
        Indice_Group = opt['indices']
        Num_Array = local_indice_map(Indice_Group)
        Cal_Index = np.array(Num_Array).shape[0]
        Dex = np.zeros((Count, Cal_Index))

    m = 0
    M = 0

    Q = Robot.qlim
    N_DoF, _ = Q.shape
    QUpL = Q[:, 1]
    QDownL = Q[:, 0]
    qUp = QUpL.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    qDown = QDownL.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    if opt['evaluate'] == 'Off':
        for i in range(Count):
            TQS = Robot.fkine(QS[i])
            TQS=np.array(TQS)
            TQS = TQS.T
            Dex[i,0] = TQS[0,3]
            Dex[i,1] = TQS[1,3]
            Dex[i,2] = TQS[2,3]
    elif opt['evaluate'] == 'On':
        for i in range(Count):
            All_T = Robot.fkine(QS[i,:])
            All_T=np.array(All_T)
            print(All_T)
            print(All_T[0,3])
            Mid_Point[i,0] = All_T[0,3]
            Mid_Point[i,1] = All_T[1,3]
            Mid_Point[i,2] = All_T[2,3]
            qPtr = QS[i].ctypes.data_as(ctypes.POINTER(ctypes.c_double))
            if Joint_Flag == 1:
                R[i,0] = joint_limitation(qPtr, qUp, qDown, N_DoF)
            else:
                R[i,0] = 1
            TQS = All_T
            Dex[i,0] = TQS[0,3]
            Dex[i,1] = TQS[1,3]
            Dex[i,2] = TQS[2,3]
            Y = ERobot.jacobe(Robot,QS[i])
            for K in range(Cal_Index):
                Evaluation = Indice_Group[K]
                #print(Num_Array[0],Indice_Group[0])
                Dex[i ,K] = local_evaluation(Indice_Group[K], N_DoF, Y, m, M, R[i, 0])
                if Evaluation.startswith('Dynamic'):
                    M = ERobot.inertia(Robot, QS[i])
                    m = dynamic_M(Robot, QS[i])

    #Norminization
    _, Dex_Indice_Num = Dex.shape
    for i in range(3, Dex_Indice_Num):
        Max_Value = np.max(Dex[:, i])
        Dex[:, i] /= Max_Value

    if opt['save'] == 'Save':
        np.save(path, Dex)
    elif opt['save'] == 'UnSave':
        path = 'N'



    Overall_Point = Dex[:, 0:3]
    Data = np.vstack((Overall_Point, Mid_Point))

    # O_Volume = qhull.ConvexHull(Data).volume
    # Volume = qhull.ConvexHull(Overall_Point).volume

    return Dex, path
           # O_Volume, Volume
