import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for  i in range(len(arr1)):
    if (i % 2) == 0: # even index           
        print("O número ", i , " é par")