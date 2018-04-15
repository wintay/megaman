import numpy as np
from PIL import ImageGrab
import cv2
import time
from getkeys import key_check
import os
import pyautogui

def keys_to_output(keys):
	#[Z,X,C,left,up,right,down]
    output = [0,0,0,0,0,0,0]
    if 'Z' in keys:
        output[0] = 1
        # print('z')
    if 'X' in keys:
        output[1] = 1
        # print('x')
    if 'C' in keys:
        output[2] = 1
        # print('c')
    if 'J' in keys:
        output[3] = 1
        # print('left')
    if 'I' in keys:
        output[4] = 1
        # print('up')
    if 'L' in keys:
        output[5] = 1
        # print('right')
    if 'K' in keys:
        output[6] = 1
        # print('down')
    if 'P' in keys:
        np.save(file_name,training_data)
        print('saved')
    print(output)
    return output
file_name ='trainingdata.npy'
if os.path.isfile(file_name):
    print ('loading')
    training_data = list(np.load(file_name))
else:
    print('creating file')
    training_data = []

def process_img(original_image):
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    keys = key_check()
    output = keys_to_output(keys)
    training_data.append([processed_img,output])
    return processed_img

# Controls
def left():
    pyautogui.keyDown('j')
    pyautogui.keyUp('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyUp('z')
    pyautogui.keyUp('x')

def right():
    pyautogui.keyUp('j')
    pyautogui.keyDown('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyUp('z')
    pyautogui.keyUp('x')

def jump():
    pyautogui.keyUp('j')
    pyautogui.keyUp('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyDown('z')
    pyautogui.keyUp('x')

def shoot():
    pyautogui.keyUp('j')
    pyautogui.keyUp('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyUp('z')
    pyautogui.press('x')

def ladder_up():
    pyautogui.keyUp('j')
    pyautogui.keyUp('l')
    pyautogui.keyDown('i')
    pyautogui.keyUp('k')
    pyautogui.keyUp('z')
    pyautogui.keyUp('x')

def ladder_down():
    pyautogui.keyUp('j')
    pyautogui.keyUp('l')
    pyautogui.keyUp('i')
    pyautogui.keyDown('k')
    pyautogui.keyUp('z')
    pyautogui.keyUp('x')

def jump_right():
    pyautogui.keyUp('j')
    pyautogui.keyDown('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyDown('z')
    pyautogui.keyUp('x')

def jump_left():
    pyautogui.keyDown('j')
    pyautogui.keyUp('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyDown('z')
    pyautogui.keyUp('x')

def stop():
    pyautogui.keyUp('j')
    pyautogui.keyUp('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyUp('z')
    pyautogui.keyUp('x')

# Countdown
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

last_time = time.time()
while(True):
    # 800x600
    # 40 px accounts for title bar. 
    screen = np.array(ImageGrab.grab(bbox=(0,40, 800, 640)))
    new_screen = process_img(screen)#display processed img

    #print('jump')
    #PressKey(Z)
    #time.sleep(3)
    #print('fire')
    #PressKey(X)

    #print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

    cv2.imshow('window', new_screen)
    if len(training_data) % 500 == 0 :
        np.save(file_name,training_data)
        print('saved')
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# screen_record()

#VID9 10.21