from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def boundary_ws(dex, value, color='off'):
    data = dex[:, :3]
    print(data)
    hull = ConvexHull(data)
    print(hull)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if color == 'r':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2], triangles=hull.simplices, edgecolor='r', facecolor='r', alpha=value)
    elif color == 'b':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2], triangles=hull.simplices, edgecolor='b', facecolor='b', alpha=value)
    elif color == 'g':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2], triangles=hull.simplices, edgecolor='g', facecolor='g', alpha=value)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

