import numpy as np
Num= np.arange(1,20)
mask= Num % 2==1
print("odd Number:" , Num[mask])
idx= [0,5,10]
print("selected num:",Num[idx])