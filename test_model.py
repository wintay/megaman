import numpy as np
from PIL import ImageGrab
import cv2
import time
# import pyautogui
from directkeys import PressKey,ReleaseKey, Z, X, J, K, L, I
from getkeys import key_check
from alexnet import alexnet
# import tensorflow as tf

WIDTH = 195
HEIGHT = 175
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'megaman-learningai-mtl-v2-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

# Controls
def left():
    ReleaseKey(Z)
    # ReleaseKey(X)
    PressKey(J)
    ReleaseKey(L)

def right():
    ReleaseKey(Z)
    # ReleaseKey(X)
    ReleaseKey(J)
    PressKey(L)

def jump():
    PressKey(Z)
    # ReleaseKey(X)
    ReleaseKey(J)
    ReleaseKey(L)

def shoot():
    # ReleaseKey(Z)
    # PressKey(X)
    # ReleaseKey(J)
    # ReleaseKey(L)
    PressKey(X)
    ReleaseKey(X)

# def ladder_up():
#     pyautogui.keyUp('j')
#     pyautogui.keyUp('l')
#     pyautogui.keyDown('i')
#     pyautogui.keyUp('k')
#     pyautogui.keyUp('z')
#     pyautogui.keyUp('x')

# def ladder_down():
#     pyautogui.keyUp('j')
#     pyautogui.keyUp('l')
#     pyautogui.keyUp('i')
#     pyautogui.keyDown('k')
#     pyautogui.keyUp('z')
#     pyautogui.keyUp('x')

def jump_right():
    PressKey(Z)
    # ReleaseKey(X)
    ReleaseKey(J)
    PressKey(L)

def jump_left():
    PressKey(Z)
    # ReleaseKey(X)
    PressKey(J)
    ReleaseKey(L)

def stop_moving():
    ReleaseKey(Z)
    # ReleaseKey(X)
    ReleaseKey(J)
    ReleaseKey(L)

# def shoot_right():
#     pyautogui.keyUp('j')
#     pyautogui.keyDown('l')
#     pyautogui.keyUp('z')
#     pyautogui.keyDown('x')

# def shoot_left():
#     pyautogui.keyDown('j')
#     pyautogui.keyUp('l')
#     pyautogui.keyUp('z')
#     pyautogui.keyDown('x')

# def shoot_jump():
#     pyautogui.keyUp('j')
#     pyautogui.keyUp('l')
#     pyautogui.keyDown('z')
#     pyautogui.keyDown('x')

def main():
    model = alexnet(WIDTH, HEIGHT, LR)
    model.load(MODEL_NAME)

    last_time = time.time()

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        
    paused = False
    walk_th = 0.7
    shoot_th = 0.1
    jump_th = 0.5
    stop_ct = 0 # prevent infinite freeze
    # max_stop_ct = 25
    max_stop_ct = 500

    while(True):
        # 800x600 windowed mode
        screen = np.array(ImageGrab.grab(bbox=(0,40, 390, 350)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # screen =  cv2.Canny(screen, threshold1 = 200, threshold2=300)
        # screen = cv2.resize(screen, (390,350))
        screen = cv2.resize(screen, (195,175))
        # cv2.imshow('window',screen)
        # moves = list(np.around(model.predict([screen])[0]))
        prediction = model.predict([screen.reshape(195,175,1)])[0]
        print(prediction)
        # moves = list(np.around(model.predict([screen.reshape(195,175,1)])[0]))
        # print(moves)

        # [jump, shoot, left, right, jump_left, jump_right]
        if prediction[1] > shoot_th:
            shoot()
            print('shoot')

        # if prediction[4] > jump_th:
        #     jump_left()
        #     print('jump left')
        # elif prediction[5] > jump_th:
        #     jump_right()
        #     print('jump right')
        if (prediction[2] + prediction[4]) > walk_th:
            if prediction[4] > prediction[2]:
                jump_left()
                print('jump left')
            else:
                left()
                print('left')
        elif (prediction[3] + prediction[5]) > walk_th:
            if prediction[5] > prediction[3]:
                jump_right()
                print('jump right')
            else:
                right()
                print('right')
        elif prediction[0] > jump_th:
            jump()
            print('jump')
        else:
            if stop_ct > max_stop_ct:
                stop_ct = 0
                right()
            else:
                stop_moving()
                stop_ct += 1
            print('default')

        # pause action
        keys = key_check()

        if 'P' in keys:
            if paused:
                print('unpause')
                paused = False
                time.sleep(1)
            else:
                print('pause')
                paused = True
                ReleaseKey(Z)
                ReleaseKey(X)
                ReleaseKey(J)
                ReleaseKey(L)
                time.sleep(1)

main()
