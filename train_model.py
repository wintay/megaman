import numpy as np
from alexnet import alexnet
import tflearn
import tensorflow as tf

WIDTH = 195
HEIGHT = 175
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'megaman-learningai-mtl-v2-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

# data_set = ''     # Willy Fortress 2 stage
data_set = '_mtl'   # Metalman stage

tflearn.init_graph(num_cores=6, gpu_memory_fraction=0.75, soft_placement=True)

with tf.device('/gpu:0'):
    model = alexnet(WIDTH, HEIGHT, LR)

    # # load existed model
    # model.load(MODEL_NAME)
    # print('load existed model')

    hm_data = 24
    start_at = 1
    for i in range(EPOCHS):
        for i in range(start_at, hm_data + 1):
            train_data = np.load('data\\data_balanced{}_{}.npy'.format(data_set, i))

            train = train_data[:-100]
            test = train_data[-100:]

            X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
            Y = [i[1] for i in train]

            test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
            test_y = [i[1] for i in test]

            model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
                snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

            model.save(MODEL_NAME)

# tensorboard --logdir=D:\Codespace\Training\megaman_train
