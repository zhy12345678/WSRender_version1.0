import numpy as np
import matplotlib.pyplot as plt
from basic_Matlab_to_Python.functions.basic_functions.ReadFiles import read_files

def draw_environment(*args, **kwargs):
    opt = {'visual': ['off', 'Off', 'Desk_On', 'Frame_On', 'Both_On']}
    opt.update(kwargs)

    # Read environment configuration
    config_file, Out = read_files(type='Environment')
    desk = Out[0]
    frame = Out[1]
    Desk_Length, Desk_Width, Desk_Height = desk[0], desk[1], desk[2]
    Frame_Height, Frame_Width = frame[0], frame[1]
    delta = Desk_Length / 10

    out = 'no'

    if opt['visual'] == 'off' or opt['visual'] == 'Off':
        out = 'no environment'
        plt.grid(False)
        X = np.arange(-Desk_Width, Desk_Width, 0.01)
        Y = np.arange(-Desk_Length, Desk_Length, 0.01)
        X, Y = np.meshgrid(Y, X)
        Z = X * 0
        plt.gca().plot_surface(X, Y, Z, facecolors='b', edgecolors='none', alpha=0.6)

    elif opt['visual'] == 'Desk_On':
        plt.plot([Desk_Length/2, Desk_Length/2], [Desk_Width, Desk_Width], [-Desk_Height, 0], 'k', linewidth=3)
        plt.plot([-Desk_Length/2, -Desk_Length/2], [Desk_Width, Desk_Width], [-Desk_Height, 0], 'k', linewidth=3)
        plt.plot([-Desk_Length/2, -Desk_Length/2], [0, 0], [-Desk_Height, 0], 'k', linewidth=3)
        plt.plot([Desk_Length/2, Desk_Length/2], [0, 0], [-Desk_Height, 0], 'k', linewidth=3)

        X = np.arange(0, Desk_Width, 0.01)
        Y = np.arange(-Desk_Length/2, Desk_Length/2, 0.01)
        X, Y = np.meshgrid(Y, X)
        Z = X * 0
        plt.gca().plot_surface(X, Y, Z, facecolors='b', edgecolors='none', alpha=0.6)

    elif opt['visual'] == 'Frame_On':
        plt.plot([-Frame_Width/2, Frame_Width/2], [0, 0], [Frame_Height, Frame_Height], 'r', linewidth=3)
        plt.plot([-Frame_Width/2, Frame_Width/2], [0, 0], [0, 0], 'r', linewidth=3)
        plt.plot([-(Frame_Width/2-delta), -(Frame_Width/2-delta)], [0, 0], [0, Frame_Height], 'r', linewidth=3)
        plt.plot([(Frame_Width/2-delta), (Frame_Width/2-delta)], [0, 0], [0, Frame_Height], 'r', linewidth=3)

    elif opt['visual'] == 'Both_On':
        plt.plot([Desk_Length/2, Desk_Length/2], [Desk_Width, Desk_Width], [-Desk_Height, 0], 'k', linewidth=3)
        plt.plot([-Desk_Length/2, -Desk_Length/2], [Desk_Width, Desk_Width], [-Desk_Height, 0], 'k', linewidth=3)
        plt.plot([-Desk_Length/2, -Desk_Length/2], [0, 0], [-Desk_Height, 0], 'k', linewidth=3)
        plt.plot([Desk_Length/2, Desk_Length/2], [0, 0], [-Desk_Height, 0], 'k', linewidth=3)

        X = np.arange(0, Desk_Width, 0.01)
        Y = np.arange(-Desk_Length/2, Desk_Length/2, 0.01)
        X, Y = np.meshgrid(Y, X)
        Z = X * 0
        plt.gca().plot_surface(X, Y, Z, facecolors='b', edgecolors='none', alpha=0.6)

        plt.plot([-Frame_Width/2, Frame_Width/2], [0, 0], [Frame_Height, Frame_Height], 'r', linewidth=3)
        plt.plot([-Frame_Width/2, Frame_Width/2], [0, 0], [0, 0], 'r', linewidth=3)
        plt.plot([-(Frame_Width/2-delta), -(Frame_Width/2-delta)], [0, 0], [0, Frame_Height], 'r', linewidth=3)
        plt.plot([(Frame_Width/2-delta), (Frame_Width/2-delta)], [0, 0], [0, Frame_Height], 'r', linewidth=3)

    return out

