from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH, RevoluteMDH, PrismaticMDH
import numpy as np
import roboticstoolbox as rtb

robot = DHRobot(
    [
        RevoluteDH(alpha=np.pi/2),
        RevoluteDH(a=0.4318),
        RevoluteDH(d=0.15005, a=0.0203, alpha=-np.pi/2),
        RevoluteDH(d=0.4318, alpha=np.pi/2),
        RevoluteDH(alpha=-np.pi/2),
        RevoluteDH()
    ], name="Puma560")


puma = rtb.models.DH.Puma560()
print(puma)
puma.plot(puma)