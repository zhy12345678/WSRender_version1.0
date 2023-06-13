import numpy as np

def copy_interleaved(m, n):
    #mr, mc = m.shape
    shape = m.shape
    if len(shape) == 1:
        mc, = shape
        mr = 1
    else:
        mc, mr = shape
    print(mr,mc)
    b = np.zeros((mr * n, mc))
    ind = np.arange(1,mr+1)
    B=[]
    for i in np.arange(0, n) * mr:
        print(b.shape)
        print(i)
        print(ind)
        b[ind + i-1, :] = m
        print('第',i,'次',b)
        B.append(b.tolist())
        #b[ind + i, :] = m
    print(B)
    B = np.array(B)
    #b=np.reshape(b,mr,n*mc)
    b = np.reshape(b, (mr, n * mc), order='C')
    print(b)
    return b
