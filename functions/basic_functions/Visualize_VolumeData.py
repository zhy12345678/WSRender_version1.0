import numpy as np
import matplotlib.pyplot as plt
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS import boundary_ws

def visualize_volume_data(boundary, V_left, V_right, volume_size, precision, *args):
    opt_visual = ['Off', 'Bimanual', 'Seperate', 'Scatter']
    opt_visual = parse_options(opt_visual, args)

    xminH = boundary[0, 0]
    yminH = boundary[1, 0]
    zminH = boundary[2, 0]
    V_dual_arm = V_left + V_right
    Pre = precision

    A, B, C = volume_size

    transfer_left = []
    transfer_right = []
    transfer_dual = []

    for i in range(A):
        for j in range(B):
            for k in range(C):
                if V_left[i, j, k] != 0:
                    transfer_left.append([xminH + Pre * (j - 1), yminH + Pre * (i - 1), zminH + Pre * (k - 1),
                                          V_left[i, j, k]])

                if V_right[i, j, k] != 0:
                    transfer_right.append([xminH + Pre * (j - 1), yminH + Pre * (i - 1), zminH + Pre * (k - 1),
                                           V_right[i, j, k]])

                if V_dual_arm[i, j, k] != 0:
                    transfer_dual.append([xminH + Pre * (j - 1), yminH + Pre * (i - 1), zminH + Pre * (k - 1),
                                          V_dual_arm[i, j, k]])

    transfer_left = np.array(transfer_left)
    transfer_right = np.array(transfer_right)
    transfer_dual = np.array(transfer_dual)

    if opt_visual == 'Seperate':
        plt.plot(transfer_left[:, 0], transfer_left[:, 1], transfer_left[:, 2], '*b')
        plt.hold(True)
        plt.plot(transfer_right[:, 0], transfer_right[:, 1], transfer_right[:, 2], '*r')
        plt.hold(True)
    elif opt_visual == 'Bimanual':
        plt.plot(transfer_dual[:, 0], transfer_dual[:, 1], transfer_dual[:, 2], '*g')
        Dex = transfer_dual
        v = boundary_ws(Dex, 0.1, 'g')
        plt.hold(True)
    elif opt_visual == 'Scatter':
        plt.scatter(transfer_left[:, 0], transfer_left[:, 1], transfer_left[:, 2], 5, transfer_left[:, 3])
        plt.hold(True)
        plt.scatter(transfer_right[:, 0], transfer_right[:, 1], transfer_right[:, 2], 5, transfer_right[:, 3])
        plt.hold(True)
        plt.colorbar()
        plt.grid(False)
        plt.axis('off')

    return transfer_right, transfer_left, transfer_dual


def parse_options(opt_visual, options):
    opt_visual_val = opt_visual[0]

    for option in options:
        if option in opt_visual:
            opt_visual_val = option

    return opt_visual_val





# Example usage
# Boundary = np.array([[0, 0], [0, 0], [0, 0]])
# VLeft = np.zeros((10, 10, 10))
# VRight = np.zeros((10, 10, 10))
# Volume_Size = [10, 10, 10]
# Precision = 0.1
# opt_visual = 'Bimanual'
#
# TransferRight, TransferLeft, TransferDual = visualize_volume_data(Boundary, VLeft, VRight, Volume_Size, Precision,
#                                                                    opt_visual)
# print(TransferRight)
# print(TransferLeft)
# print(TransferDual)
