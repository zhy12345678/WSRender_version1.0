import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH,PrismaticDH,RevoluteMDH,PrismaticMDH
from spatialmath import SE3
from spatialmath import base

class ABB_Yumi(DHRobot):
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
                d=0.11,
                a=0.03,
                alpha=pi/2,
                qlim=np.deg2rad([-168.5, 168.5])
            ),
            RevoluteDH(
                d=0,
                a=0.03,
                alpha=pi / 2,
                qlim=np.deg2rad([-143.5, 43.5])
            ),
            RevoluteDH(
                d=0.2465,
                a=0.0405,
                alpha=pi/2,
                qlim=np.deg2rad([-123.5, 80])
            ),
            RevoluteDH(
                d=0,
                a=0.0405,
                alpha=-pi/2,
                qlim=np.deg2rad([-290, 290])
            ),
            RevoluteDH(
                d=0.265,
                a=0.0135,
                alpha=pi/2,
                qlim=np.deg2rad([-88, 138])
            ),
            RevoluteDH(
                d=0,
                a=0.027,
                alpha=-pi/2,
                qlim=np.deg2rad([-229, 229])
            ),
            RevoluteDH(
                d=0.032,
                a=0,
                alpha=0,
                qlim=np.deg2rad([-168.5, 168.5])
            ),
        ]



        super().__init__(
            L,
            name="ABB_Yumi",
            symbolic=symbolic
        )





if __name__ == "__main__":  # pragma nocover

    ABB_Yumi = ABB_Yumi(symbolic=False)

