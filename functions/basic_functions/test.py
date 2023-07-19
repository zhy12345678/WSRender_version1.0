import numpy as np
configs = {
    1: np.array([[1. , 0. , 0. , 0.1],
             [0. , 1. , 0. , 0. ],
             [0. , 0. , 1. , 0.4],
             [0. , 0. , 0. , 1. ]]),
    2: np.array([[ 1. ,  0. ,  0. , -0.1],
             [ 0. ,  1. ,  0. ,  0. ],
             [ 0. ,  0. ,  1. ,  0.4],
             [ 0. ,  0. ,  0. ,  1. ]]),
    3: np.array([[ 0. , -1. ,  0. ,  0.1],
             [ 1. ,  0. ,  0. ,  0.4],
             [ 0. ,  0. ,  1. ,  0. ],
             [ 0. ,  0. ,  0. ,  1. ]]),
    4: np.array([[ 0. , -1. ,  0. , -0.1],
             [ 1. ,  0. ,  0. ,  0.4],
             [ 0. ,  0. ,  1. ,  0. ],
             [ 0. ,  0. ,  0. ,  1. ]]),
    5: 4
}

input_value = int(input("Enter the input value: "))

if input_value in configs:
    result = configs[input_value]
    print(result)
else:
    print("Input value not found in configs")
