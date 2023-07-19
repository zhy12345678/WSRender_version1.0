import numpy as np
import matplotlib.pyplot as plt
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS import boundary_ws

def visualize_single_volume_data(boundary, V, volume_size, precision, *args):
    opt_evaluate = ['Reachable', 'Boundary', 'Scatter']
    opt_visual = ['Bimanual', 'Seperate']
    opt_evaluate, opt_visual = parse_options(opt_evaluate, opt_visual, args)

    xminH = boundary[0, 0]
    yminH = boundary[1, 0]
    zminH = boundary[2, 0]
    V_dual_arm = V
    Pre = precision
    A, B, C = volume_size
    Total = A * B * C
    transfer_dual = np.zeros((Total, 4))
    numC = 0
    for i in range(A):
        for j in range(B):
            for k in range(C):
                if V_dual_arm[i, j, k] != 0:
                    numC += 1
                    transfer_dual[numC - 1, 0] = xminH + Pre * (j - 1)
                    transfer_dual[numC - 1, 1] = yminH + Pre * (i - 1)
                    transfer_dual[numC - 1, 2] = zminH + Pre * (k - 1)
                    transfer_dual[numC - 1, 3] = V_dual_arm[i, j, k]

    volume = 0
    if opt_evaluate == 'Reachable':
        transfer_dual[:, 3] = 1
        plt.plot(transfer_dual[:, 0], transfer_dual[:, 1], transfer_dual[:, 2], '*y')
        plt.hold(True)
    elif opt_evaluate == 'Boundary':
        volume = boundary_ws(transfer_dual, 0.1, 'g')
    else:
        plt.colormap('jet')
        plt.colorbar()
        plt.caxis([0, 1])
        plt.figure(figsize=(10, 10))
        plt.grid(False)
        plt.axis('off')
        plt.scatter(transfer_dual[:, 0], transfer_dual[:, 1], transfer_dual[:, 2], 5, transfer_dual[:, 3])
        plt.camlight('headlight', 'infinite')
        plt.hold(True)

    return transfer_dual, volume


def parse_options(opt_evaluate, opt_visual, options):
    opt_evaluate_val = opt_evaluate[0]
    opt_visual_val = opt_visual[0]

    for option in options:
        if option in opt_evaluate:
            opt_evaluate_val = option
        if option in opt_visual:
            opt_visual_val = option

    return opt_evaluate_val, opt_visual_val





# Example usage
# Boundary = np.array([[0, 0], [0, 0], [0, 0]])
# V = np.zeros((10, 10, 10))
# Volume_Size = [10, 10, 10]
# Precision = 0.1
# opt_evaluate = 'Reachable'
# opt_visual = 'Bimanual'
#
# TransferDual, Volume = visualize_single_volume_data(Boundary, V, Volume_Size, Precision, opt_evaluate, opt_visual)
# print(TransferDual)
# print(Volume)
