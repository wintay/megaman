# balance_data.py
import cv2
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import os

hm_data = 24

# data_set = ''     # Willy Fortress 2 stage
data_set = '_mtl'   # Metalman stage

for i in range(1,hm_data+1):
    file_name = 'data\\data_balanced{}_{}.npy'.format(data_set, i)
    if os.path.isfile(file_name):
        print ('file {} already exist: skipped'.format(i))
    else:
        train_data = np.load('raw_data\\trainingdata{}_{}.npy'.format(data_set, i))
        df = pd.DataFrame(train_data)
        print(df.head())

        newdata = []

        for data in train_data:
            img = data[0]
            choice = data[1]

            # # convert old data from 4-input to 6-input
            # if choice != [0,0,0,0]:
            #     if choice[0] == 1 and choice[2] == 1:
            #         choice = [0,0,0,0,1,0]
            #     elif choice[0] == 1 and choice[3] == 1:
            #         choice = [0,0,0,0,0,1]
            #     else:
            #         choice.extend([0,0])

            if choice != [0,0,0,0,0,0]:
                newdata.append([img,choice])
            # else:
            # 	print('no matches')

        np.save(file_name, newdata)
        print('create file {}'.format(i))

print('done!')

#for data in train_data:
#    img = data[0]
#    choice = data[1]
#    cv2.imshow('test',img)
#    print(choice)
#    if cv2.waitKey(25) & 0xFF == ord('q'):
#        cv2.destroyAllWindows()
#        break
