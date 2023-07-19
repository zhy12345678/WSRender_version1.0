from typing import List
from collections import defaultdict
from basic_Matlab_to_Python.functions.basic_functions.ReadFiles import read_files


def local_indice_map(indice_group):
    print(indice_group)
    num = len(indice_group)
    print(num)
    num_array = [0] * num
    print(num_array)

    _, index_name = read_files(type='All_Indices')
    print(index_name)
    all_num = len(index_name)
    all_index_num = list(range(4, 4 + all_num))
    map_local_index = dict(zip(all_index_num, index_name))
    map_inv_local_index = {v: k for k, v in map_local_index.items()}

    num_array = []
    for element in indice_group:
        if element in index_name.values():
            index = [key for key, value in index_name.items() if value == element][0]
            num_array.append(map_inv_local_index[index])
        else:
            num_array.append(None)

    return num_array

'''
一个对于这个函数的测试
index_name = {
    1: 'Manipulability',
    2: 'Inverse Condition Number',
    3: 'Minimum Singular Value',
    4: 'Order-Independent Manipulability',
    5: 'Harmonic Mean Manipulability Index',
    6: 'Isotropic Index',
    7: 'Dynamic Manipulability',
    8: 'Dynamic Inverse Condition Number',
    9: 'Dynamic Minimum Singular Value',
    10: 'Dynamic Order-Independent Manipulability',
    11: 'Dynamic Harmonic Mean Manipulability Index',
    12: 'Dynamic Isotropic Index'
}

map_inv_local_index = {
    1: 4,
    2: 5,
    3: 6,
    4: 7,
    5: 8,
    6: 9,
    7: 10,
    8: 11,
    9: 12,
    10: 13,
    11: 14,
    12: 15
}

indice_group = ['Manipulability', 'Inverse Condition Number', 'Isotropic Index']

indices = []
for element in indice_group:
    if element in index_name.values():
        index = [key for key, value in index_name.items() if value == element][0]
        indices.append(map_inv_local_index[index])
    else:
        indices.append(None)

print(indices)

'''