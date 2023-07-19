"""
% Input:
% opt.type
%
% Output:
% N_Dof: number of degrees of freedom
% Robot: the robot model built by the pre-defined DH Table
%
% Function:
% Build a targeted robot for workspace analysis
% Define a robot based on DH table;
% Define joint limitation
% Basic type:
% Articulated robot; Spherical robot; Cartesian robot; etc.
% Self-defined robot: 'Define'
%
% Example:
% [N_DoF,Robot] = BuildRobot('Articulated');

"""
import numpy as np
from basic_Matlab_to_Python.buildRobot.Puma560 import Puma560
from basic_Matlab_to_Python.buildRobot.Cylindrical import Cylindrical
from basic_Matlab_to_Python.buildRobot.Articulated import Articulated
from basic_Matlab_to_Python.buildRobot.Catersian import Catersian
from basic_Matlab_to_Python.buildRobot.dVRK import dVRK
from basic_Matlab_to_Python.buildRobot.HamlynCRM import HamlynCRM
from basic_Matlab_to_Python.buildRobot.MIS import MIS
from basic_Matlab_to_Python.buildRobot.Omni import Omni
from basic_Matlab_to_Python.buildRobot.Redandant import Redandant
from basic_Matlab_to_Python.buildRobot.SCARA import SCARA
from basic_Matlab_to_Python.buildRobot.Spherical import Spherical
from basic_Matlab_to_Python.buildRobot.Underactuated import Underactuated
from basic_Matlab_to_Python.buildRobot.ABB_Yumi import ABB_Yumi
from basic_Matlab_to_Python.buildRobot.DefineRobot1 import define_robot1

from basic_Matlab_to_Python.functions.basic_functions.DefineRobot import define_robot
from basic_Matlab_to_Python.functions.basic_functions.tb_optparse_forone import tb_optparse_forone

def BuildOneRobot(*args):
    print(args)
    deg = np.pi / 180
    opt = {'type': ['Articulated', 'Spherical', 'Cylindrical', 'Catersian', 'SCARA', 'dVRK', 'Omni', 'HamlynCRM','Redandant',
                    'ABB_Yumi', 'Puma560', 'Underactuated', 'MIS', 'Full_Human_Arm', 'DefineRobot1','DefineRobot2']}
    #opt = tb_optparse(opt, args)
    opt=tb_optparse_forone(opt,args[0])
    print(opt)
    N_Dof=0


    if opt['type'] == 'Articulated':
        Robot = Articulated()
        N_Dof = Robot.N_Dof

    elif opt['type'] == 'Spherical':
        Robot = Spherical()
        N_Dof = Robot.N_Dof


    elif opt['type'] == 'Cylindrical':
        Robot=Cylindrical()
        N_Dof=Robot.N_Dof


    elif opt['type'] == 'Catersian':
        Robot = Catersian()
        N_Dof = Robot.N_Dof


    elif opt['type'] == 'SCARA':
        Robot = SCARA()
        N_Dof = Robot.N_Dof

    elif opt['type'] == 'Underactuated':
        Robot = Underactuated()
        N_Dof = Robot.N_Dof


    elif opt['type'] == 'Redandant':
        Robot = Redandant()
        N_Dof = Robot.N_Dof



    elif opt['type'] == 'dVRK':
        Robot = dVRK()
        N_Dof = Robot.N_Dof


    elif opt['type'] == 'MIS':
        Robot = MIS()
        N_Dof = Robot.N_Dof


    elif opt['type'] == 'ABB_Yumi':
        Robot = ABB_Yumi()
        N_Dof = Robot.N_Dof

    elif opt['type'] == 'HamlynCRM':
        Robot = HamlynCRM()
        N_Dof = Robot.N_Dof


    elif opt['type']=='Omni':
        Robot = Omni()
        N_Dof = Robot.N_Dof

    elif opt['type']=='Puma560':
        Robot = Puma560()
        N_Dof = Robot.N_Dof


    elif opt['type']=='DefineRobot1':
        # Robot=define_robot1()
        # N_Dof=Robot.N_Dof
        N_Dof, Robot = define_robot(1)


    return Robot, N_Dof
