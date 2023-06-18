import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH, RevoluteMDH, PrismaticMDH
from spatialmath import SE3
from spatialmath import base


class Omni(DHRobot):
    """
    Class that models a Cylindrical manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool
     can be used as Cylindrical

    .. runblock:: pycon

        >>> import basic_Matlab_to_Python as bp
        >>> robot = bp.buildRobot.Omni()
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


        L = [
            RevoluteDH(
                d=0,
                a=0,
                alpha=0,
                qlim=np.deg2rad([-50,  50])
            ),
            RevoluteDH(
                d=0,
                alpha=pi / 2,
                a=0,
                qlim=np.deg2rad([0 , 105])
            ),
            RevoluteDH(
                alpha=0,
                a=0.127508,
                d=0,
                qlim=np.deg2rad([-90 , 0])
            ),
            RevoluteDH(
                d=0,
                a=0.149352,
                alpha=pi/2,
                qlim=np.deg2rad([-180, 180])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=-pi / 2,
                qlim=np.deg2rad([ 20 , 160])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi / 2,
                qlim=np.deg2rad([-70,  70])
            ),
        ]

        super().__init__(
            L,
            name="Omni",
            symbolic=symbolic
        )


if __name__ == "__main__":  # pragma nocover

    Omni = Omni(symbolic=False)
    # print(HamlynCRM)
    # print(HamlynCRM.dynamics())


