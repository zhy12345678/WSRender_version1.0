"""
Load Existing Local indices distribution map and visualze
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt #是python的专门的画图包3D
import scipy.io
from mpl_toolkits.mplot3d import Axes3D

pwd = r'G:\United Kindom\毕设\WSRender\WSRender_V0.0-master\WSRender_V0.0-master'
current_folder = os.getcwd()
os.chdir(pwd)
sys.path.append(pwd)


file_name = r'G:\United Kindom\毕设\WSRender\WSRender_V0.0-master\WSRender_V0.0-master\Data\dVRK216000.mat'
# file = np.load(file_name,allow_pickle=True)
file = scipy.io.loadmat(file_name) # 在python中引用.mat 的matlab形式的文件时，不能用一般的方法load,应该用scripy
dex = file['Dex'] #将从.mat文件加载的' dex '变量的值赋给dex。
dex_left = dex.copy()
dex_left[:, 1] += 0.2 #作为index的副本创建，第二列增加0.2

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d') #创建带有3D子图的图形。
ax.scatter(dex[:, 0], dex[:, 1], dex[:, 2], c=dex[:, 3], s=5, cmap='viridis')
ax.scatter(dex_left[:, 0], dex_left[:, 1], dex_left[:, 2], c=dex_left[:, 3], s=5)
ax.set_xlabel('X') #设定坐标轴的用法
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d(np.min(dex[:, 0]), np.max(dex[:, 0])) #根据限制进行绘图
ax.set_ylim3d(np.min(dex[:, 1]), np.max(dex[:, 1]))
ax.set_zlim3d(np.min(dex[:, 2]), np.max(dex[:, 2]))
fig.colorbar(ax.get_children()[0], ax=ax)

plt.show()


file_name = r'G:\United Kindom\毕设\WSRender\WSRender_V0.0-master\WSRender_V0.0-master\Data\Spherical3375.mat'
file = scipy.io.loadmat(file_name)
dex = file['Dex']
dex_left = dex.copy()
dex_left[:, 1] += 0.2

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dex[:, 0], dex[:, 1], dex[:, 2], c=dex[:, 3], s=5, cmap='viridis')
ax.scatter(dex_left[:, 0], dex_left[:, 1], dex_left[:, 2], c=dex_left[:, 3], s=5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d(np.min(dex[:, 0]), np.max(dex[:, 0]))
ax.set_ylim3d(np.min(dex[:, 1]), np.max(dex[:, 1]))
ax.set_zlim3d(np.min(dex[:, 2]), np.max(dex[:, 2]))
fig.colorbar(ax.get_children()[0], ax=ax)

plt.show()
