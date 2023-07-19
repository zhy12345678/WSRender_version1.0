import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH,PrismaticDH,RevoluteMDH,PrismaticMDH
from spatialmath import SE3
from spatialmath import base

class define_robot2(DHRobot):
    """
    Class that models a Cylindrical manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool
     can be used as Cylindrical

    .. runblock:: pycon

        >>> import basic_Matlab_to_Python as bp
        >>> robot = bp.buildRobot.ABB_Yumi()
        >>> print(robot)
    """

    def __init__(self, symbolic=False):

        self.N_Dof = 7


        if symbolic:
            import spatialmath.base.symbolic as sym
            zero = sym.zero()
            pi = sym.pi()
        else:
            from math import pi
            zero = 0.0

        deg = pi / 180
        inch = 0.0254
        base = 26.45 * inch  # from mounting surface to shoulder axis


        L=[
            RevoluteDH(
                d=0,
                a=0,
                alpha=0,
                theta=pi/2,
                I=[0, 0.35, 0, 0, 0, 0],
                r=[0, 0, 0],
                m=0,
                Jm=200e-6,
                G=-62.6111,
                B=1.48e-3,
                Tc=[0.395, -0.435],
                modified=True,
                qlim=np.deg2rad([-70, 70])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=-pi / 2,
                I=[0.13, 0.524, 0.539, 0, 0, 0],
                r=[-0.3638, 0.006, 0.2275],
                m=17.4,
                B=.817e-3,
                Tc=[0.126, -0.071],
                modified=True,
                qlim=np.deg2rad([20, 160])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi/2,
                I=[0.066, 0.086, 0.0125, 0, 0, 0],
                r=[-0.0203, -0.0141, 0.070],
                m=4.8,
                Jm=200e-6,
                G=-53.7063,
                B=1.38e-3,
                Tc=[0.132, -0.105],
                modified=True,
                qlim=np.deg2rad([-180, 180])
            ),
            PrismaticDH(
                theta=-pi/2,
                modified=True,
                d=0,
                a=0,
                alpha=0,
                qlim=np.deg2rad([15/deg,20/deg])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=0,
                I=[0, 0.35, 0, 0, 0, 0],
                r=[0, 0, 0],
                m=0,
                Jm=200e-6,
                G=-62.6111,
                B=1.48e-3,
                Tc=[0.395, -0.435],
                modified=True,
                qlim=np.deg2rad([-180, 180])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=-pi / 2,
                I=[0.13, 0.524, 0.539, 0, 0, 0],
                r=[-0.3638, 0.006, 0.2275],
                m=17.4,
                Jm=200e-6,
                G=107.815,
                B=.817e-3,
                Tc=[0.126, -0.071],
                modified=True,
                qlim=np.deg2rad([20, 160])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi / 2,
                I=[0.066, 0.086, 0.0125, 0, 0, 0],
                r=[-0.0203, -0.0141, 0.070],
                m=4.8,
                Jm=200e-6,
                G=-53.7063,
                B=1.38e-3,
                Tc=[0.132, -0.105],
                modified=True,
                qlim=np.deg2rad([-70, 70])
            ),
        ]



        super().__init__(
            L,
            name="define_robot2",
            symbolic=symbolic
        )





if __name__ == "__main__":  # pragma nocover

    define_robot2 = define_robot2(symbolic=False)

