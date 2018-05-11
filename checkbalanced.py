import cv2
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

data_set = ''     # Willy Fortress 2 stage
# data_set = '_mtl'   # Metalman stage

train_data = np.load('data\\data_balanced{}_3.npy'.format(data_set))

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test',img)
    print(choice)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break