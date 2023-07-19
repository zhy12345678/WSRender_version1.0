from spatialmath import *
from spatialmath.base import *
from spatialmath import UnitQuaternion
import numpy as np
#用T2方法打印出来的矩阵看起来更舒服
T1 = transl(0.5, 0.0, 0.0) @ rpy2tr(0.1, 0.2, 0.3, order='xyz') @ trotx(-90, 'deg')
print(T1)
T2=SE3(0.5,0,0)*SE3.RPY([0.1,0.2,0.3],order='xyz')*SE3.Rx(-90,unit='deg')
print(T2)
T2.eul() # 新坐标系的方向可以用欧拉角表示 用来确定定点转动刚体位置的3个一组独立角参量，由章动角θ、旋进角（即进动角）ψ和自转角φ组成，为欧拉首先提出而得名。
print(T2.eul)
T2.R#并且可以提取组件，例如旋转子矩阵
print(T2.R)
T2.t#平移子矩阵？？不懂输出的也不是平移啊
print(T2.t)

T2.plot(color='red',label='2') #

print(UnitQuaternion.Rx(0.3))
print(UnitQuaternion.AngVec(0.3,[1,0,0]))

R=SE3.Rx(np.linspace(0,np.pi/2,num=100))
print(R)
print(len(R))
