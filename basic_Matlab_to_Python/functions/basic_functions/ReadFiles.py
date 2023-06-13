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

        out[1] = desk
        out[2] = frame

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
        # T = np.eye(4)
        T=np.zeros((5, 4))
        k = 1
        i = 1
        r = 0

        with open(config_file, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)

            # Find the robot number
            for idx, line in enumerate(lines):
                if line.strip() == "#Robot Number":
                    robot_num = int(lines[idx + 1])
                    break

            # Find the transformation matrices
            while k < num_lines:
                line = lines[k].strip()

                if line.startswith("#Transformation Matrix"):
                    #T = np.eye(4)
                    T = np.zeros((5,4))
                    f = 0
                    r = 1
                    k += 1
                    continue

                if r != 0 and line != '':
                    row = [float(num) for num in line.split()]
                    T[i, :] = row
                    i += 1

                    if i == 5:
                        # out[k] = T
                        out[k]=T[1:5,:]
                        r = 0
                        k += 1
                        i = 1

                k += 1

            out[k] = robot_num

            # Find the robot names
            k = 1
            for idx, line in enumerate(lines):
                if line.strip() == f"#Robot Type{k}":
                    robots_name.append(lines[idx + 1].strip())
                    k += 1


    return robots_name, out

'''
一个readfiles函数的测试代码
from ReadFiles import read_files
robots_name, out = read_files(type='Indices')
print(robots_name)
print(out)
'''




