"""
% Input:
% Robot: the robot model in Matlab
% Flag: Couple_Flag
%
% Option:
% opt.type = {'General','MentoCarlo'};
% 'MentoCarlo': Mento Carlo method for joint generation
% 'JointNum': define the number of segmentation of each joint
% opt.save = {'Save','UnSave'};
%
% Output:
% QS: Joint Value Combination Map
% Count: Number of the pose
%
% Function:
% Generate joint value combination map, a list of pose
%
% Example:
% [QS,Count]=Generate_Joint(Robot,1,'MentoCarlo','JointNum',15);

%%
"""
import numpy as np
import roboticstoolbox as rtb

def generate_joint(Robot, Flag, **kwargs):
    opt = {
        'JointNum': None,
        'type': 'General',
        'save': 'Save',
        'Path': None
    }
    opt.update(kwargs)
    #因为在一开始的时候传入的robot的结构是Robot: Tuple[SerialLink, int] = BuildOneRobot(robot_type)但是属性是只有SerialLink有的所以需要进行一些调整
    #robot_tuple = BuildOneRobot(robot_type)
    serial_link_object = Robot[0]  # Access the SerialLink object from the tuple
    #qlim_attribute = serial_link_object.qlim  # Access the qlim attribute on the SerialLink object

    #N_DoF, _ = Robot.qlim.shape
    N_DoF, _ =serial_link_object.qlim.shape

    #Q = Robot.qlim
    Q=serial_link_object.qlim

    QUp = Q[:, 1]
    QDown = Q[:, 0]

    if opt['JointNum'] is None:
        N = 15
    else:
        N = opt['JointNum']

    if opt['Path'] is None:
        filename = 'Joint_Map'
        path_Joint = './Data/Joint_Map'
    else:
        filename = opt['Path']
        path_Joint = f"./Data/{filename}{N}"

    if Flag == 0:
        N_Joint = N_DoF - 3
    else:
        N_Joint = N_DoF

    Count = N ** N_Joint
    QS = np.zeros((Count, N_DoF))

    if Flag == 0:
        for k in range(N_Joint):
            I = N_DoF + 1 - k
            QS[:, I-1] = (Q[I-1, 0] + Q[I-1, 1]) / 2

    Joint_Table = np.zeros((N_Joint, N))

    if opt['type'] == 'General':
        for i in range(N_Joint):
            Joint_Table[i, :] = np.linspace(QDown[i], QUp[i], N)
        QS_P = Mycombvec(Joint_Table)
        QS_P = np.transpose(QS_P)
        QS[:, :N_Joint] = QS_P

    elif opt['type'] == 'MentoCarlo':
        for i in range(N_Joint):
            QS[:, i] = QDown[i] + (QUp[i] - QDown[i]) * np.random.rand(1, Count)

    if opt['save'] == 'Save':
        np.save(path_Joint, QS)
    else:
        out = 'UnSave'

    return QS, Count
