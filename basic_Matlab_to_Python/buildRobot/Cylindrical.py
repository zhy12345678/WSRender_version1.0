import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH,PrismaticDH,RevoluteMDH,PrismaticMDH
from spatialmath import SE3
from spatialmath import base

class Cylindrical(DHRobot):
    """
    Class that models a Cylindrical manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool
     can be used as Cylindrical

    .. runblock:: pycon

        >>> import basic_Matlab_to_Python as bp
        >>> robot = bp.buildRobot.Cylindrical()
        >>> print(robot)
    """

    def __init__(self, symbolic=False):

        self.N_Dof = 6

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
                d=0.2,
                a=0,
                alpha=0,
                qlim=np.deg2rad([-45 , 45])
            ),
            PrismaticDH(
                alpha=-pi/2,
                a=0,
                qlim=np.deg2rad([0.0/deg , 0.40/deg])
            ),
            PrismaticDH(
                alpha=-pi/2,
                a=0,
                qlim=np.deg2rad([0.20/deg , 0.40/deg])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=0,
                qlim=np.deg2rad([-180,  180])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=np.deg2rad([20 ,160])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=np.deg2rad([-70, 70])
            ),
        ]

        # Robot = SerialLink([L1, L2, L3, L4, L5, L6], name='Cylindrical')

        super().__init__(
            L,
            name="Cylindrical",
            symbolic=symbolic
        )





if __name__ == "__main__":  # pragma nocover

    Cylindrical = Cylindrical(symbolic=False)
    # print(Cylindrical)
    # print(Cylindrical.dynamics())

    # T = puma.fkine(puma.qn)
    # print(puma.ikine_a(T, 'lu').q)
    # print(puma.ikine_a(T, 'ru').q)
    # print(puma.ikine_a(T, 'ld').q)
    # print(puma.ikine_a(T, 'rd').q)

    # puma.plot(puma.qz)
