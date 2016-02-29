
import numpy as np


a = np.ones((2,4,3))


print a.reshape((2,-1))

print a

data = {'X_train':1,'y_train':2,'X_val':3,'y_val':4    }