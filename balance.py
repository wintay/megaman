# balance_data.py
import cv2
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('trainingdata.npy')
df = pd.DataFrame(train_data)
print(df.head())

newdata = []
for data in train_data:
    img = data[0]
    choice = data[1]

    if choice != [0,0,0,0,0,0,0]:
    	newdata.append([img,choice])
    else:
    	print('no matches')

np.save('balanced_data.npy', newdata)

#for data in train_data:
#    img = data[0]
#    choice = data[1]
#    cv2.imshow('test',img)
#    print(choice)
#    if cv2.waitKey(25) & 0xFF == ord('q'):
#        cv2.destroyAllWindows()
#        break
