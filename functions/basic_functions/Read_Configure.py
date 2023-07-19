import os

def read_configure(file_name):
    folder = os.getcwd()
    target_file = os.path.join(folder, 'Data', file_name)

    with open(target_file, 'r') as file:
        data = [list(map(float, line.strip().split())) for line in file]

    b = [[row[i] for i in range(3)] for row in data]

    return b
