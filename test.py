import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, W, A, S, D, X, Z, C, left, up, right, down
from getkeys import key_check
import os

def keys_to_output(keys):
	#[Z,X,C,left,up,right,down]
	output = [0,0,0]
	if 'Z' in keys:
		output[0] = 1
	elif 'X' in keys:
		output[1] = 1
	elif 'C' in keys:
		output[2] = 1
	elif 'left' in keys:
		output[3] = 1
	elif 'up' in keys:
		output[4] = 1
	elif 'right' in keys:
		output[5] = 1
	elif 'down' in keys:
		output[6] = 1
	return output		

def process_img(original_image):
    
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


last_time = time.time()
while(True):
    # 800x600
    # 40 px accounts for title bar. 
    screen = np.array(ImageGrab.grab(bbox=(0,40, 800, 640)))
    new_screen = process_img(screen)

    #print('jump')
    #PressKey(Z)
    #time.sleep(3)
    #print('fire')
    #PressKey(X)

    print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow('window', new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

screen_record()

#VID9 10.21