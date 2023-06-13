import numpy as np

def copy_blocked(m, n):
    #mr, mc = m.shape
    shape = m.shape
    if len(shape) == 1:
        mc, = shape
        mr = 1
    else:
        mr, mc = shape
    b = np.zeros((mr, mc * n))
    ind = np.arange(1,mc+1)
    B =[]
    for i in np.arange(0, n) * mc:
        print(b.shape)
        print(i)
        print(ind)
        b[:, ind + i -1] = m
        #print('第',i,'次',b)
        B.append(b.tolist())
    print(B)
    return B
'''
这个最后输出的格式为
 1     2     3     0     0     0     0     0     0
 1     2     3     1     2     3     0     0     0
 1     2     3     1     2     3     1     2     3
'''