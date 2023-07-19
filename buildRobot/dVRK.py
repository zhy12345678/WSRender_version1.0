import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH,PrismaticDH,RevoluteMDH,PrismaticMDH
from spatialmath import SE3
from spatialmath import base

class dVRK(DHRobot):
    """
    Class that models a Cylindrical manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool
     can be used as Cylindrical

    .. runblock:: pycon

        >>> import basic_Matlab_to_Python as bp
        >>> robot = bp.buildRobot.dVRK()
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
        Length1 = 0.2794;
        Length2 = 0.3048;


        L=[
            RevoluteDH(
                d=0,
                a=0,
                alpha=0,
                qlim=np.deg2rad([-40 , 65])
            ),
            RevoluteDH(
                d=0,
                alpha=-pi/2,
                a=0,
                qlim=np.deg2rad([-15, 50])
            ),
            RevoluteDH(
                d=0,
                alpha=0,
                a=Length1,
                qlim=np.deg2rad([-50 , 35])
            ),
            RevoluteDH(
                d=0.1506,
                a=Length2,
                alpha=pi/2,
                qlim=np.deg2rad([-200 ,90])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=-pi/2,
                qlim=np.deg2rad([-90 , 180])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=np.deg2rad([-45 , 45])
            ),
        ]



        super().__init__(
            L,
            name="dVRK",
            symbolic=symbolic
        )





if __name__ == "__main__":  # pragma nocover

    dVRK = dVRK(symbolic=False)
    # print(dVRK)
    # print(dVRK.dynamics())

    # T = puma.fkine(puma.qn)
    # print(puma.ikine_a(T, 'lu').q)
    # print(puma.ikine_a(T, 'ru').q)
    # print(puma.ikine_a(T, 'ld').q)
    # print(puma.ikine_a(T, 'rd').q)

    # puma.plot(puma.qz)
