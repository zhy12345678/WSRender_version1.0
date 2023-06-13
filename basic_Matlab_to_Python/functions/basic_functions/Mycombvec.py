# %COMBVEC Create all combinations of vectors.
# %
# %  <a href="matlab:doc combvec">combvec</a>(A1,A2,...) takes any number of inputs A, where each Ai has
# %  Ni columns, and return a matrix of (N1*N2*...) column vectors, where
# %  the columns consist of all combinations found by combining one column
# %  vector from each Ai.
# %
# %  For instance, here the four combinations of two 2-column matrices are
# %  found.
# %
# %    a1 = [1 2 3; 4 5 6];
# %    a2 = [7 8; 9 10];
# %    a3 = <a href="matlab:doc combvec">combvec</a>(a1,a2)
#
# % Mark Beale, 12-15-93
# % Copyright 1992-2010 The MathWorks, Inc.

import numpy as np
from basic_Matlab_to_Python.functions.basic_functions.Mycombvec_copy_blocked import copy_blocked
from basic_Matlab_to_Python.functions.basic_functions.Mycombvec_copy_interleaved import copy_interleaved

def Mycombvec(M):
    rows, _ = M.shape

    if len(M) == 0:
        return np.array([])
    else:
        y = M[0, :]
        for i in range(1, rows):
            z = M[i, :]
            X=copy_blocked(y, z.shape[0])
            Y=copy_interleaved(z, y.shape[0])
            y = np.hstack((X,Y))
        return y





# Example usage
M = np.array([[1, 2, 3], [4, 5, 6]])
y = Mycombvec(M)
print(y)
