import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH,PrismaticDH,RevoluteMDH,PrismaticMDH
from spatialmath import SE3
from spatialmath import base

class Underactuated(DHRobot):
    """
    Class that models a Cylindrical manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool
     can be used as Cylindrical

    .. runblock:: pycon

        >>> import basic_Matlab_to_Python as bp
        >>> robot = bp.buildRobot.SCARA()
        >>> print(robot)
    """

    def __init__(self, symbolic=False):

        self.N_Dof = 5


        if symbolic:
            import spatialmath.base.symbolic as sym
            zero = sym.zero()
            pi = sym.pi()
        else:
            from math import pi
            zero = 0.0

        deg = pi / 180
        Length=0.30


        L=[
            RevoluteDH(
                d=0,
                a=0,
                alpha=0,
                qlim=np.deg2rad([-160 , -20])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=np.deg2rad([-140 , 140])
            ),
            RevoluteDH(
                d=0,
                a=Length,
                alpha=0,
                qlim=np.deg2rad([-140, 140])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=np.deg2rad([20,  160])
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi/2,
                qlim=np.deg2rad([-90, 90])
            ),
        ]



        super().__init__(
            L,
            name="SimpleArm",
            symbolic=symbolic
        )





if __name__ == "__main__":  # pragma nocover

    Underactuated = Underactuated(symbolic=False)

