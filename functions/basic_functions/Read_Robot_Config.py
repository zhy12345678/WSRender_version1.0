import  numpy as np


def read_robot_config(config_file):
    Out = {}
    Robots_Name = []

    with open(config_file, 'r') as file:
        robot_num = None
        T = np.eye(4)
        k = 1
        f = 0
        r = 0
        i = 1

        for line in file:
            line = line.strip()

            if line == "#Robot Number":
                line = next(file).strip()
                robot_num = int(line)

            if line.startswith("#Transformation Matrix"):
                T = np.eye(4)
                f = 0
                r = 1

            if r != 0 and line and not line.startswith("#"):
                row = list(map(float, line.split()))
                T[i - 1, :] = row
                i += 1
                if i == 5:
                    Out[k] = T
                    r = 0
                    k += 1
                    i = 1

        Out[k] = robot_num

    with open(config_file, 'r') as file:
        k = 1

        for line in file:
            line = line.strip()

            if line.startswith('#Robot Type'):
                line = next(file).strip()
                Robots_Name.append(line)
                k += 1

    return Out, Robots_Name


# config_file = 'Rob_config.txt'
# Out, Robots_Name = read_robot_config(config_file)
# print(Out)
# print(Robots_Name)

