import numpy as np
growth = np.array([0.7,0.2,0.5])
rain = np.array([[40,50,60],[20,35,25],[30,40,55]])
print(growth[:,None]*rain)
