'''
% Input:
% Dex: local indices distribution map
% Pre: precision degree
% BaseRight: right manipulator base coordinate
% BaseLeft: left manipulator base coordinate
% Option:
%     opt.evaluate = {'Manipulability','InverseCN','MSV'};
%     opt.visual = {'Visual_Off','Visual_On'};
%     opt.bimanual={'Single','BimanualRobot','BimanualArm'};
%
% Output:
% VDualArm: bimanual robot overall workspace
% VLeft: left manipulator volume data
% VRight: right manipulator volume data
% Boundary: boundary of the volume data
% Volume_Size: size of the volume data
%
% Function:
% Convert single/bimanual robot local indices distribution map to volume data mode
%
% Example:
'''
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from skimage import measure



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def scatter_to_volume(Dex, Pre, BaseRight, BaseLeft, **kwargs):
    opt = {
        'save': 'UnSave',
        'visual': 'Visual_Off',
        'bimanual': 'Single'
    }
    opt.update(kwargs)

    if opt['bimanual'] == 'BimanualArm':
        Left = Dex[:, [0, 1, 2, 3]] - np.array([0.20, 0, 0, 0])
        Right = Dex[:, [0, 1, 2, 3]]
    elif opt['bimanual'] == 'BimanualRobot':
        Left = Dex[:, [0, 1, 2, 3]] + np.array(BaseLeft)
        Right = Dex[:, [0, 1, 2, 3]] + np.array(BaseRight)

    Count, _ = Right.shape
    Boundary = np.zeros((3, 2))

    xminH = np.min(Left[:, 0])
    xmaxH = np.max(Right[:, 0])
    yminH = np.min(Left[:, 1])
    ymaxH = np.max(Left[:, 1])
    zminH = np.min(Left[:, 2])
    zmaxH = np.max(Left[:, 2])

    Boundary[0, 0] = xminH
    Boundary[0, 1] = xmaxH
    Boundary[1, 0] = yminH
    Boundary[1, 1] = ymaxH
    Boundary[2, 0] = zminH
    Boundary[2, 1] = zmaxH

    xxH, yyH, zzH = np.meshgrid(
        np.arange(xminH, xmaxH + Pre, Pre),
        np.arange(yminH, ymaxH + Pre, Pre),
        np.arange(zminH, zmaxH + Pre, Pre)
    )

    A, B, C = xxH.shape
    Volume_Size = [A, B, C]

    VLeft = np.zeros(xxH.shape)
    VRight = np.zeros(xxH.shape)

    for i in range(Count):
        aa = np.round((Left[i, 0] - xminH) / Pre).astype(int)
        aaR = np.round((Right[i, 0] - xminH) / Pre).astype(int)
        bb = np.round((Left[i, 1] - yminH) / Pre).astype(int)
        cc = np.round((Left[i, 2] - zminH) / Pre).astype(int)

        if cc == 0 or cc < 0:
            cc = 1

        if bb == 0 or bb < 0:
            bb = 1

        if aaR == 0 or aaR < 0:
            aaR = 1

        if aa == 0 or aa < 0:
            aa = 1

        if cc > C:
            cc = C

        if bb > A:
            bb = A

        if aaR > B:
            aaR = B

        if aa > B:
            aa = B

        VLeft[bb, aa, cc] = Left[i, 3]
        VRight[bb, aaR, cc] = Right[i, 3]

    VDualArm = VLeft + VRight

    if opt['visual'] == 'Visual_On':
        iso_val = 0.5

        vertices_left, faces_left, _, _ = measure.marching_cubes(VLeft, iso_val)
        normals_left = measure.mesh_surface_area(vertices_left, faces_left)

        vertices_right, faces_right, _, _ = measure.marching_cubes(VRight, iso_val)
        normals_right = measure.mesh_surface_area(vertices_right, faces_right)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        pD_left = Poly3DCollection(vertices_left[faces_left], alpha=0.3)
        ax.add_collection(pD_left)
        pD_left.set_facecolor('green')
        pD_left.set_edgecolor('none')

        pD_right = Poly3DCollection(vertices_right[faces_right], alpha=0.3)
        ax.add_collection(pD_right)
        pD_right.set_facecolor('green')
        pD_right.set_edgecolor('none')

        pD_left.set_normals(normals_left)
        pD_right.set_normals(normals_right)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

    return VDualArm, VLeft, VRight, Boundary, Volume_Size
