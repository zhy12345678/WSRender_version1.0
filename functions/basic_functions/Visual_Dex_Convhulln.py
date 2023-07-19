import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def visual_dex_convhulln(right, left, *args):
    opt_visual = ['Single', 'Bimanual', 'Off']
    opt_visual = parse_options(opt_visual, args)

    P_left = left[:, :3]
    K, Volume_L = convhulln(P_left)

    new_surf = np.zeros((K.shape[0], 3))

    for i in range(K.shape[0]):
        new_surf[i, 0] = left[K[i], 0]
        new_surf[i, 1] = left[K[i], 1]
        new_surf[i, 2] = left[K[i], 2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.add_collection(Poly3DCollection([new_surf], alpha=0.3, facecolor=(0.667, 1, 0)))
    plt.colorbar()
    ax.view_init(elev=30, azim=120)

    Volume_R = 0
    P_right = right[:, :3]
    K, Volume_R = convhulln(P_right)

    new_surf = np.zeros((K.shape[0], 3))

    for i in range(K.shape[0]):
        new_surf[i, 0] = right[K[i], 0]
        new_surf[i, 1] = right[K[i], 1]
        new_surf[i, 2] = right[K[i], 2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.add_collection(Poly3DCollection([new_surf], alpha=0.3, facecolor=(0, 0.667, 1)))
    plt.colorbar()
    ax.view_init(elev=30, azim=120)

    return Volume_R, Volume_L


def parse_options(opt_visual, options):
    opt_visual_val = opt_visual[0]

    for option in options:
        if option in opt_visual:
            opt_visual_val = option

    return opt_visual_val


def convhulln(points):
    num_points = points.shape[0]
    num_dimensions = points.shape[1]

    indices = np.arange(num_points)
    combinations = np.vstack([np.roll(indices, -i) for i in range(num_dimensions)])
    facet_combinations = combinations[:, :-1].T

    point_vectors = points[facet_combinations].transpose(2, 0, 1)
    facet_vectors = np.cross(point_vectors[:, 1] - point_vectors[:, 0],
                             point_vectors[:, 2] - point_vectors[:, 0])
    facet_normals = facet_vectors / np.linalg.norm(facet_vectors, axis=1)[:, None]

    is_convex = np.all(np.dot(facet_normals, points.T) <= np.max(np.dot(facet_normals, points.T)), axis=0)
    visible_facets = facet_combinations[:, is_convex]

    volume = 0
    if num_dimensions == 3:
        visible_facet_vectors = points[visible_facets].transpose(2, 0, 1)
        volume = np.abs(np.sum(np.einsum('ijk,ik->i', visible_facet_vectors[:, :-1],
                                         visible_facet_vectors[:, -1])) / 6)

    return visible_facets, volume


# Example usage
# Right = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
# Left = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
# opt_visual = 'Bimanual'
#
# Volume_R, Volume_L = visual_dex_convhulln(Right, Left, opt_visual)
# print(Volume_R)
# print(Volume_L)
