import numpy as np
from alexnet import alexnet
import tflearn
import tensorflow as tf

WIDTH = 195
HEIGHT = 175
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'megaman-learningai-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

tflearn.init_graph(num_cores=6, gpu_memory_fraction=0.75, soft_placement=True)

with tf.device('/gpu:0'):
    model = alexnet(WIDTH, HEIGHT, LR)

    # hm_data = 22
    for i in range(EPOCHS):
        # for i in range(1,hm_data+1):
        train_data = np.load('balanced_data.npy')

        train = train_data[:-100]
        test = train_data[-100:]

        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

        model.save(MODEL_NAME)
