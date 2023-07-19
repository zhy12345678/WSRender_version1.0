import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
from matplotlib.patches import Polygon


def VisualWS(Dex, *args, **kwargs):
    opt = {
        'evaluate': ['Reachable', 'Local_Indices'],
        'robotnum': ['SingleArm', 'Bimanual'],
        'color': ['y', 'g', 'r', 'b'],
        'vector': [],
        'Index': []
    }
    opt.update(kwargs)
    out = 1

    Vector = opt['vector'] if len(opt['vector']) != 0 else [0, 0, 0, 0, 0, 0]

    #Vector = opt['vector'] if opt['vector'] else [0, 0, 0, 0, 0, 0]
    Num = opt['Index'] if opt['Index'] else 4

    if opt['evaluate'] == 'Reachable':
        if opt['robotnum'] == 'SingleArm':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot3D(Dex[:, 0], Dex[:, 1], Dex[:, 2], opt['color'])
            plt.show()
        elif opt['robotnum'] == 'Bimanual':
            Dex_Right = Dex[:, :3] + Vector[:3]
            Dex_Left = Dex[:, :3] + Vector[3:]
            hull_right = ConvexHull(Dex_Right)
            hull_left = ConvexHull(Dex_Left)

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.add_collection(Polygon(Dex_Right[hull_right.vertices], alpha=0.1, facecolor='b', edgecolor='b'))
            ax.add_collection(Polygon(Dex_Left[hull_left.vertices], alpha=0.1, facecolor='b', edgecolor='b'))
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            plt.show()

    elif opt['evaluate'] == 'Local_Indices':
        if opt['robotnum'] == 'SingleArm':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(Dex[:, 0], Dex[:, 1], Dex[:, 2], c=Dex[:, Num], s=5)
            plt.colorbar()
            plt.show()
        elif opt['robotnum'] == 'Bimanual':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(Dex[:, 0] + Vector[0], Dex[:, 1] + Vector[1], Dex[:, 2] + Vector[2], c=Dex[:, Num], s=5)
            ax.scatter(Dex[:, 0] + Vector[3], Dex[:, 1] + Vector[4], Dex[:, 2] + Vector[5], c=Dex[:, Num], s=5)
            plt.colorbar()
            plt.show()

    return out
