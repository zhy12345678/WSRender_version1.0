import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH,PrismaticDH,RevoluteMDH,PrismaticMDH
from spatialmath import SE3
from spatialmath import base

class Redandant(DHRobot):
    """
    Class that models a Cylindrical manipulator

    :param symbolic: use symbolic constants
    :type symbolic: bool
     can be used as Cylindrical

    .. runblock:: pycon

        >>> import basic_Matlab_to_Python as bp
        >>> robot = bp.buildRobot.Redandant()
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



        L=[
            RevoluteDH(
                d=0,
                a=0,
                alpha=0
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=-pi/2
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi / 2
            ),
            PrismaticDH(
                theta=-pi/2,
                a=0,
                alpha=0,
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=0
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=-pi/2
            ),
            RevoluteDH(
                d=0,
                a=0,
                alpha=pi/2
            ),
        ]



        super().__init__(
            L,
            name="Redandant",
            symbolic=symbolic
        )





if __name__ == "__main__":  # pragma nocover

    Redandant = Redandant(symbolic=False)

