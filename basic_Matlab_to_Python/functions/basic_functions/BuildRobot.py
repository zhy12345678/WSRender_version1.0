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
from roboticstoolbox import SerialLink,Link
from roboticstoolbox import RevoluteDH
from roboticstoolbox import RevoluteMDH #MDH比DH更加的灵活
from basic_Matlab_to_Python.functions.basic_functions.DefineRobot import define_robot
from basic_Matlab_to_Python.functions.basic_functions.tb_optparse import tb_optparse
from roboticstoolbox.robot.ERobot import ERobot



def BuildRobot(*args):
    print(args[0])
    deg = np.pi / 180
    opt = {'type': ['Articulated', 'Spherical', 'Cylindrical', 'Catersian', 'SCARA', 'dVRK', 'Omni', 'HamlynCRM',
                    'ABB_Yumi', 'Puma560', 'Underactuated', 'MIS', 'Full_Human_Arm', 'Define']}
    #opt = tb_optparse(opt, args)
    Robot=[]
    N_Dof=[]



    if opt['type'] == 'Articulated':
        L1 = RevoluteMDH(d=0, a=0, alpha=0, **{'modified': True})
        L2 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, **{'modified': True})
        L3 = RevoluteMDH(d=0, a=0.20, alpha=0, **{'modified': True})
        L4 = RevoluteMDH(d=0, a=0.20, alpha=np.pi / 2, **{'modified': True})
        L5 = RevoluteMDH(d=0, a=0, alpha=-np.pi / 2, **{'modified': True})
        L6 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, **{'modified': True})

        Robot = SerialLink([L1, L2, L3, L4, L5, L6])
        Robot.qlim = np.deg2rad([[45, 135], [-45, 45], [-120, 0], [-180, 180], [20, 160], [-70, 70]])
        Robot.name = 'Articualted'
        N_Dof = 6

    elif opt['type'] == 'Spherical':
        L1 = RevoluteMDH(d=0, a=0, alpha=0, **{'modified': True})
        L2 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, **{'modified': True})
        L3 = Link(theta=0, alpha=-np.pi / 2, a=0, **{'modified': True})
        L4 = RevoluteMDH(d=0, a=0, alpha=0, **{'modified': True})
        L5 = RevoluteMDH(d=0, a=0, alpha=-np.pi / 2, **{'modified': True})
        L6 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, **{'modified': True})


        Robot = SerialLink([L1, L2, L3, L4, L5, L6])
        Robot.qlim = np.deg2rad([[-45, 45], [45, 135], [0.20 / deg, 0.40 / deg], [-180, 180], [20, 160], [-70, 70]])
        Robot.name = 'Spherical'
        N_Dof = 6


    elif opt['type'] == 'Cylindrical':
        L1 = RevoluteMDH(d=0.20, a=0, alpha=0, **{'modified': True})
        L2 = Link(theta=0, alpha=-np.pi / 2, a=0, **{'modified': True})
        L3 = Link(theta=0, alpha=-np.pi / 2, a=0, **{'modified': True})
        L4 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, **{'modified': True})
        L5 = RevoluteMDH(d=0, a=0, alpha=0, **{'modified': True})
        L6 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, **{'modified': True})


        Robot = SerialLink([L1, L2, L3, L4, L5, L6])
        Robot.qlim = np.deg2rad([[0, 180], [-180, 180], [-180, 180], [45, 135], [-180, 180], [-180, 180]])
        Robot.name = 'Cylindrical'
        N_Dof = 6

    elif opt['type'] == 'Cartesian':
        L1 = Link(theta=0, alpha=-np.pi / 2, a=0, **{'modified': True})
        L2 = Link(theta=0, alpha=np.pi / 2, a=0, **{'modified': True})
        L3 = RevoluteMDH(d=0, a=0.20, alpha=0, **{'modified': True})
        L4 = RevoluteMDH(d=0, a=0.20, alpha=0, **{'modified': True})
        L5 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, **{'modified': True})
        L6 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, **{'modified': True})


        Robot = SerialLink([L1, L2, L3, L4, L5, L6])
        Robot.qlim = np.deg2rad([[-180, 180], [-180, 180], [-120, 0], [-180, 180], [-180, 180], [-180, 180]])
        Robot.name = 'Cartesian'
        N_Dof = 6

    elif opt['type'] == 'SCARA':
        L1 = RevoluteDH(d=0, a=0.2, alpha=0, **{'modified': True})
        L2 = RevoluteDH(d=0, a=0.2, alpha=0, **{'modified': True})
        L3 = Link(theta=0, alpha=-np.pi / 2, a=0, **{'modified': True})
        L4 = RevoluteDH(d=0, a=0, alpha=0, **{'modified': True})


        # Create the SCARA robot
        Robot = SerialLink([L1, L2, L3, L4])
        # Set the joint limits
        Robot.qlim = np.deg2rad( [[45, 135], [45, 135], [0.20 / deg, 0.40 / deg], [-180, 180], [20, 160], [-70, 70]])
        Robot.name = 'SCARA'
        N_Dof = 4

    elif opt['type'] == 'Underactuated':
        # Define the robot parameters
        Length = 0.30
        L1 = RevoluteMDH(d=0, a=0, alpha=0, modified=True)
        L2 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, modified=True)
        L3 = RevoluteMDH(d=0, a=Length, alpha=0, modified=True)
        L4 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, modified=True)
        L5 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, modified=True)
        N_Dof = 5
        # Create the simplified arm model
        Robot = SerialLink([L1, L2, L3, L4, L5], name='SimpleArm')
        # Set the joint limits
        qlim_deg = [-160, -20, -140, 140, -140, 140, 20, 160, -90, 90]  # Joint limits in degrees
        qlim_rad = np.deg2rad(qlim_deg)  # Convert degrees to radians
        Robot.qlim = np.reshape(qlim_rad, (-1, 2))

        # Optionally set the robot's name
        Robot.name = 'SimpleArm'


    elif opt['type'] == 'Full_Human_Arm':

        # Full_Human_Arm
        L1 = RevoluteMDH(d=0, a=0, alpha=0, modified=True)
        L2 = RevoluteMDH(d=0, a=0, alpha=-np.pi/2, modified=True)
        L3 = RevoluteMDH(d=0, a=0, alpha=np.pi/2, modified=True)
        L4 = RevoluteMDH(theta=-np.pi/2, alpha=0, a=0, modified=True)
        L4.sigma = 1
        L5 = RevoluteMDH(d=0, a=0, alpha=0, modified=True)
        L6 = RevoluteMDH(d=0, a=0, alpha=-np.pi/2, modified=True)
        L7 = RevoluteMDH(d=0, a=0, alpha=np.pi/2, modified=True)

        N_Dof = 7
        Robot = SerialLink([L1, L2, L3, L4, L5, L6, L7], name='Full_Human_Arm')

    elif opt['type'] == 'dVRK':

        Length1 = 0.2794
        Length2 = 0.3048

        L1 = RevoluteMDH(d=0, a=0, alpha=0, modified=True)
        L2 = RevoluteMDH(d=0, a=0, alpha=-np.pi / 2, modified=True)
        L3 = RevoluteMDH(d=0, a=Length1, alpha=0, modified=True)
        L4 = RevoluteMDH(d=0.1506, a=Length2, alpha=np.pi / 2, modified=True)
        L5 = RevoluteMDH(d=0, a=0, alpha=-np.pi / 2, modified=True)
        L6 = RevoluteMDH(d=0, a=0, alpha=np.pi / 2, modified=True)


        Robot = SerialLink([L1, L2, L3, L4, L5, L6], name='dVRK')
        Robot.qlim = np.deg2rad([-40, 65, -15, 50, -50, 35, -200, 90, -90, 180, -45, 45])
        N_Dof = 6

    elif opt['type'] == 'MIS':
        L1 = RevoluteMDH(d=0, a=0, alpha=0, modified=True)
        L2 = RevoluteMDH(d=0, a=0, alpha=np.pi/2, modified=True)
        L3 = Link(theta=0, alpha=-np.pi/2, a=0, modified=True)
        L3.sigma = 1
        L4 = RevoluteMDH(d=0, a=0, alpha=0, modified=True)
        L5 = RevoluteMDH(d=0, a=0, alpha=-np.pi/2, modified=True)
        L6 = RevoluteMDH(d=0, a=0, alpha=np.pi/2, modified=True)

        N_Dof = 6
        Robot = SerialLink([L1, L2, L3, L4, L5, L6], name='MIS')
        Robot.qlim = np.deg2rad([-30, 30, 60, 120, 0, 0.10/np.deg2rad(1), -180, 180, 20, 160, -70, 70])


    elif opt['type'] == 'ABB_Yumi':
        # Define the robot links
        L1 = RevoluteDH(d=0.11, a=0.03, alpha=np.pi/2, modified=True)
        L2 = RevoluteDH(d=0, a=0.03, alpha=np.pi/2, modified=True)
        L3 = RevoluteDH(d=0.2465, a=0.0405, alpha=-np.pi/2, modified=True)
        L4 = RevoluteDH(d=0, a=0.0405, alpha=-np.pi/2, modified=True)
        L5 = RevoluteDH(d=0.265, a=0.0135, alpha=-np.pi/2, modified=True)
        L6 = RevoluteDH(d=0, a=0.027, alpha=-np.pi/2, modified=True)
        L7 = RevoluteDH(d=0.032, a=0, alpha=0, modified=True)

        # Define the number of degrees of freedom
        N_Dof = 7

        # Create the robot
        Robot = SerialLink([L1, L2, L3, L4, L5, L6, L7], name='ABB_Yumi')

        # Set the joint limits in radians
        qlim_deg = [-168.5, 168.5, -143.5, 43.5, -123.5, 80, -290, 290, -88, 138, -229, 229, -168.5, 168.5]
        qlim_rad = np.deg2rad(qlim_deg)
        Robot.qlim = np.reshape(qlim_rad, (-1, 2))

    elif opt['type'] == 'HamlynCRM':
        # 'HamlynCRM' robot
        L1 = RevoluteDH(d=0, a=0, alpha=0, modified=True)
        L2 = RevoluteDH(d=0, a=0, alpha=np.pi / 2, modified=True)
        L3 = Link(theta=0, alpha=-np.pi / 2, a=0, modified=True)
        L3.sigma = 1
        L4 = RevoluteDH(d=0, a=0, alpha=0, modified=True)
        L5 = RevoluteDH(d=0, a=0, alpha=-np.pi / 2, modified=True)
        L6 = RevoluteDH(d=0, a=0, alpha=np.pi / 2, modified=True)

        N_Dof = 6
        Robot = SerialLink([L1, L2, L3, L4, L5, L6], name='HamlynCRM')
        Robot.qlim = np.deg2rad([-45, 45, 0.24 / np.deg, 0.40 / np.deg, -180, 180, 20, 160, -70, 70])


    elif opt['type']=='Omni':
        L1 = RevoluteDH(d=0, a=0, alpha=0, modified=True)
        L2 = RevoluteDH(d=0, a=0, alpha=np.pi / 2, modified=True)
        L3 = RevoluteDH(d=0, a=0.127508, alpha=0, modified=True)
        L4 = RevoluteDH(d=0, a=0.149352, alpha=np.pi / 2, modified=True)
        L5 = RevoluteDH(d=0, a=0, alpha=-np.pi / 2, modified=True)
        L6 = RevoluteDH(d=0, a=0, alpha=np.pi / 2, modified=True)

        N_Dof = 6
        Robot = SerialLink([L1, L2, L3, L4, L5, L6], name='Omni')
        Robot.qlim = np.deg2rad([-50, 50, 0, 105, -90, 0, -180, 180, 20, 160, -70, 70])

    elif opt['type']=='Puma560':
        a2 = 0.4318
        a3 = 0.0202
        d3 = 0.1244
        d4 = 0.4318

        theta1 = 0.0  # Joint angle 1
        theta2 = 0.0  # Joint angle 2
        theta3 = 0.0  # Joint angle 3
        theta4 = 0.0  # Joint angle 4
        theta5 = 0.0  # Joint angle 5
        theta6 = 0.0  # Joint angle 6

        L1 = Link(theta=[theta1, 0, 0, 0], modified=True)
        L2 = Link(theta=[theta2, 0, 0, -np.pi / 2], modified=True)
        L3 = Link(theta=[theta3, d3, a2, 0], modified=True)
        L4 = Link(theta=[theta4, d4, a3, -np.pi / 2], modified=True)
        L5 = Link(theta=[theta5, 0, 0, np.pi / 2], modified=True)
        L6 = Link(theta=[theta6, 0, 0, -np.pi / 2], modified=True)

        N_Dof = 6
        Robot = SerialLink([L1, L2, L3, L4, L5, L6], name='Puma560')

    elif opt['type']=='Define':
        N_Dof, Robot = define_robot(1)

    return Robot, N_Dof
