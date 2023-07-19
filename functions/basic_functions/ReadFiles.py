# Input:
#  Option?
# opt.type = {'Environment','Placement','Parameters','Indices','All_Indices'};
#  default?
#  type = 'Environment';
#
#  Output:
#  Config_file: List of robots
#  Out: Struct, contents of config/environment txt files
#
#  Function:
#  Read configurations
#
#  Example:
#  [file_dir,Configs] = ReadFiles('Placement');
import os
from basic_Matlab_to_Python.functions.basic_functions.Read_Robot_Config import read_robot_config
import numpy as np


def read_files(*args, **kwargs):
    opt = {
        'type': ['Environment', 'Placement', 'Parameters', 'Indices', 'All_Indices']
    }
    #
    opt.update(kwargs)
    print(opt['type'])


    robots_name = []
    out = {}

    folder = 'G:\\United Kindom\\毕设\\pyqt_design\\basic_Matlab_to_Python'
    print(folder)

    file_name = ''
    config_file = ''

    if opt['type'] == 'Environment':
        print(opt['type'])
        file_name = 'Env_config.txt'
        config_file = os.path.join(folder, 'Config', file_name)
        print(config_file)
        with open(config_file, 'r') as file_id:
            for line in file_id:
                if line.strip() == '#Desk':
                    tline = next(file_id)
                    desk = [float(num) for num in tline.split()]
                elif line.strip() == '#Frame':
                    tline = next(file_id)
                    frame = [float(num) for num in tline.split()]

        out[0] = desk
        out[1] = frame

    elif opt['type'] == 'Indices':
        p = 0
        file_name = 'Indices_config.txt'
        config_file = os.path.join(folder, 'Config', file_name)
        with open(config_file, 'r') as file_id:
            for line in file_id:
                p += 1
                out[p] = line.strip()

    elif opt['type'] == 'All_Indices':
        p = 0
        file_name = 'All_Indices.txt'
        config_file = os.path.join(folder, 'Config', file_name)
        with open(config_file, 'r') as file_id:
            for line in file_id:
                p += 1
                out[p] = line.strip()

    elif opt['type'] == 'Parameters':
        file_name = 'Parameters_config.txt'
        config_file = os.path.join(folder, 'Config', file_name)
        with open(config_file, 'r') as file_id:
            for line in file_id:
                if line.strip() == '#Couple':
                    tline = next(file_id)
                    out['Couple_Flag'] = int(tline)
                elif line.strip() == '#Joint Limit':
                    tline = next(file_id)
                    out['Joint_Flag'] = int(tline)
                elif line.strip() == '#Mento Carlo':
                    tline = next(file_id)
                    out['Mento_Flag'] = int(tline)
                elif line.strip() == '#Iteration':
                    tline = next(file_id)
                    out['Iteraction_Flag'] = int(tline)
                elif line.strip() == '#Joint Num':
                    tline = next(file_id)
                    out['Joint_Num'] = int(tline)
                elif line.strip() == '#Precision':
                    tline = next(file_id)
                    out['Precision'] = float(tline)
                elif line.strip() == '#Error':
                    tline = next(file_id)
                    out['Error'] = float(tline)

    elif opt['type'] == 'Placement':
        file_name = 'Rob_config.txt'
        config_file = os.path.join(folder, 'Config', file_name)
        Out, Robots_Name=read_robot_config(config_file)
        robots_name=Robots_Name
        out=Out



    return robots_name, out

'''
一个readfiles函数的测试代码
from ReadFiles import read_files
robots_name, out = read_files(type='Indices')
print(robots_name)
print(out)
'''




