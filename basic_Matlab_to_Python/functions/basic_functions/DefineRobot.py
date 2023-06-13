import numpy as np
from roboticstoolbox import Link, SerialLink
from roboticstoolbox import RevoluteMDH,RevoluteDH


def define_robot(index):
    if index == 1:
        l1 = 0
        l2 = 65
        l3 = 65
        l4 = 25.5
        l5 = 35

        L1 = Link(theta=(np.pi) / 2, a=0, alpha=-(np.pi) / 2)
        L2 = Link(theta=0, a=0, alpha=(np.pi) / 2)
        L3 = RevoluteMDH(d=0, a=l4, alpha=-(np.pi) / 2)
        L4 = Link(theta=0, a=0, alpha=0)

        Robot = SerialLink([L1, L2, L3, L4], name='New_Microrobot')
        Robot.qlim = np.array(
            [[0, 40], [l3, l3 + 40], [-(np.pi) / 4 + (np.pi) / 2, (np.pi) / 4 + (np.pi) / 2], [l5, l5 + 40]])

        N_Dof = 4
   # 这个自定义这里的函数还是可以进行一些改变的，可以更灵活一点
    elif index == 2:
        deg = np.pi / 180

        L1 = RevoluteMDH(d=0, a=0, alpha=0, I=[0, 0.35, 0, 0, 0, 0], r=[0, 0, 0], m=0, Jm=200e-6, G=-62.6111, B=1.48e-3,
                      Tc=[0.395, -0.435], modified=True)
        L2 = RevoluteMDH(d=0, a=0, alpha=-np.pi / 2, I=[0.13, 0.524, 0.539, 0, 0, 0], r=[-0.3638, 0.006, 0.2275], m=17.4,
                      Jm=200e-6, G=107.815, B=.817e-3, Tc=[0.126, -0.071], modified=True)
        L3 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, I=[0.066, 0.086, 0.0125, 0, 0, 0], r=[-0.0203, -0.0141, 0.070], m=4.8,
                      Jm=200e-6, G=-53.7063, B=1.38e-3, Tc=[0.132, -0.105], modified=True)
        L4 = Link(theta=-np.pi / 2, alpha=0, a=0, modified=True)
        L4.sigma = 1
        L5 = RevoluteMDH(d=0, a=0, alpha=0, I=[0, 0.35, 0, 0, 0, 0], r=[0, 0, 0], m=0, Jm=200e-6, G=-62.6111, B=1.48e-3,
                      Tc=[0.395, -0.435], modified=True)
        L6 = RevoluteMDH(d=0, a=0, alpha=-np.pi / 2, I=[0.13, 0.524, 0.539, 0, 0, 0], r=[-0.3638, 0.006, 0.2275], m=17.4,
                      Jm=200e-6, G=107.815, B=.817e-3, Tc=[0.126, -0.071], modified=True)
        L7 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, I=[0.066, 0.086, 0.0125, 0, 0, 0], r=[-0.0203, -0.0141, 0.070], m=4.8,
                      Jm=200e-6, G=-53.7063, B=1.38e-3, Tc=[0.132, -0.105], modified=True)

        Robot = SerialLink([L1, L2, L3, L4, L5, L6, L7], name='MyRobot')

        Robot.qlim = np.array(
            [[-70, 70], [20, 160], [-180, 180], [(15 / deg), (20 / deg)], [-180, 180], [20, 160], [-70, 70]])

        N_Dof = 7

    return N_Dof, Robot
