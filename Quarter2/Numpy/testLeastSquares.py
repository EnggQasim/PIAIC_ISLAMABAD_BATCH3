import sys
import numpy as np
import leastSquares


def main():
    dataFn = sys.argv[1]
    data = np.genfromtxt(dataFn, delimiter=',')
    a,b,c = leastSquares.findCoefficients(data)
    print("a=",a)
    print("b=",b)
    print("c=",c)

if __name__ == "__main__":
    main()
    
    


