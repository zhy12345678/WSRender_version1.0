"""
Input:
Robot: the robot model in Matlab
Flag: Couple_Flag
Option:
opt.type = {'General','MentoCarlo'};
'MentoCarlo': Mento Carlo method for joint generation
'JointNum': define the number of segmentation of each joint
opt.save = {'Save','UnSave'};

Output:
QS: Joint Value Combination Map
Count: Number of the pose

Function:
Generate joint value combination map, a list of pose
Example:
[QS,Count]=Generate_Joint(Robot,1,'MentoCarlo','JointNum',15);
"""
import itertools
import os
import numpy as np

def generate_joint(Robot, Flag, **kwargs):
    opt = {
        'JointNum': None,
        'type': 'General',
        'save': 'Save',
        'Path': None
    }
    opt.update(kwargs)
    _,N_DoF=Robot.qlim.shape
    Q=Robot.qlim

    QUp = Q[1, :]
    QDown = Q[0, :]

    if opt['JointNum'] is None:
        N = 15
    else:
        N = opt['JointNum']

    if opt['Path'] is None:
        filename = 'Joint_Map'
        path_Joint = '../Data_QS/Joint_Map'
    else:
        filename = opt['Path']
        path_Joint = f"../Data_QS/{filename}{N}.csv"
    #os.makedirs(os.path.dirname(path_Joint), exist_ok=True)

    if Flag == 0:
        N_Joint = N_DoF - 3
    else:
        N_Joint = N_DoF

    Count = N ** N_Joint
    QS = np.zeros((int(Count), N_DoF))


    if Flag == 0:
        for k in range(N_Joint):
            I = N_DoF  - k
            QS[:, I-1] = (Q[0, I-1] + Q[1 ,I-1]) / 2

    Joint_Table = np.zeros((N_Joint, N))

    if opt['type'] == 'General':
        for i in range(N_Joint):
            Joint_Table[i, :] = np.linspace(QDown[i], QUp[i], N)
        #QS_P = list(itertools.product(Joint_Table[0],Joint_Table[1],Joint_Table[2]))
        QS_P = list(itertools.product(*Joint_Table))
        QS[:, :N_Joint] = QS_P

    elif opt['type'] == 'MentoCarlo':
        for i in range(N_Joint):
            QS[:, i] = QDown[i] + (QUp[i] - QDown[i]) * np.random.rand(1, Count)


    if opt['save'] == 'Save':
        qs = QS
        # with open(path_Joint, 'wb') as file:
        #     file.write(qs)
        np.savetxt(path_Joint,qs,delimiter=',')
    elif opt['save'] == 'UnSave':
        out = 'UnSave'

    #np.savetxt('matrix.csv', qs, delimiter=',')
    print(qs)
    return qs, Count
