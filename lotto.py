from numba import jit
import numpy as np

TILL = 1126
ACTUAL = np.array([4,5,9,11,37,40])

#@jit(nopython=False)
def main(rand:np.random):
    candidate = np.array([i for i in range(1,46)])
    lot = rand.choice(candidate, size=6, replace=False)
    return lot

if __name__ == "__main__":
    lotto = []
    '''
    for i in range(0,TILL):
        lotto = main()
    print(sorted(lotto))
    '''
    count = 1
    rand = np.random
    rand.seed(seed=1)
    
    while(True):
        lotto = sorted(main(rand))
        #print(lotto)
        if  np.array_equal(lotto,ACTUAL):
            print("lotto is: ", lotto, " and count is ", count)
            break
        else:
            count = count + 1