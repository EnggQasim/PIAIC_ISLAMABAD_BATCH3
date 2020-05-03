def findCoefficients(arr):
    import numpy as np
    x = arr          # assignning array to a variable x
    print(x)        #printing array
    print("size of array in NxM is :", x.shape) # this array has 3 cols and 2 rows
    xx = np.array([[1], [1]])                   #extra column of ones for calculation 
    xxx=np.append(x,xx, axis=1)
    print("The array is:", xxx)
    Y=x[:,0]
    xxx[:,[1, 3]] = xxx[:,[3, 1]]
    X= xxx[:,1],xxx[:,2],xxx[:,3]
    #transpose of a matrix
    Xinv = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    #multiplication of 2 matrices
    XXinv = [[sum(a*b for a,b in zip(X_row,Xinv_col)) for Xinv_col in zip(*Xinv)] for X_row in X]    
    import numpy as np
    inverse = np.linalg.inv(XXinv)
    #multiplication of 2 matrices 
    bb = [[sum(a*b for a,b in zip(XXinv_row,Xinv_col)) for Xinv_col in zip(*Xinv)] for XXinv_row in XXinv]
    YY=Y.reshape((Y.size, 1))
    #multiplication of 2 matrices 
    COEFFICIENTS = [[sum(a*b for a,b in zip(bb_row,YY_col)) for YY_col in zip(*YY)] for bb_row in bb]
    print('COEFFICIENTS ARE c,b,a', COEFFICIENTS)
