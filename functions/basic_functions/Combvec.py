import itertools

def combvec(*args):
    return list(itertools.product(*args))

# # Example usage
# a1 = [1, 2, 3]
# a2 = [4, 5, 6]
# a3 = combvec(a1, a2)
# print(a3)