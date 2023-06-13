import os

def read_table(file_name):
    folder = os.getcwd()
    file_path = os.path.join(folder, 'Data', file_name)

    with open(file_path, 'r') as file:
        data = [list(map(float, line.split())) for line in file]

    return data
