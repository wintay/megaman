import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from alexnet import alexnet
# import tensorflow as tf

WIDTH = 195
HEIGHT = 175
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'megaman-learningai-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)

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

def shoot_right():
    pyautogui.keyUp('j')
    pyautogui.keyDown('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyUp('z')
    pyautogui.keyDown('x')

def shoot_left():
    pyautogui.keyDown('j')
    pyautogui.keyUp('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyUp('z')
    pyautogui.keyDown('x')

def shoot_jump():
    pyautogui.keyUp('j')
    pyautogui.keyUp('l')
    pyautogui.keyUp('i')
    pyautogui.keyUp('k')
    pyautogui.keyDown('z')
    pyautogui.keyDown('x')

def main():
    model = alexnet(WIDTH, HEIGHT, LR)
    model.load(MODEL_NAME)

    last_time = time.time()
    
    print('right')
    right()
    time.sleep(1)
    print('left')
    left()
    time.sleep(1)

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        
    while(True):
        # 800x600 windowed mode
        screen = np.array(ImageGrab.grab(bbox=(0,40, 390, 350)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # screen =  cv2.Canny(screen, threshold1 = 200, threshold2=300)
        # screen = cv2.resize(screen, (390,350))
        screen = cv2.resize(screen, (195,175))
        cv2.imshow('window',screen)
        # moves = list(np.around(model.predict([screen])[0]))
        moves = list(np.around(model.predict([screen.reshape(195,175,1)])[0]))
        print(moves)

        if moves == [1,0,1,0]:
            jump_left()
        elif moves == [1,0,0,1]:
            jump_right()
        elif moves == [0,1,1,0]:
            shoot_left()
        elif moves == [0,1,0,1]:
            shoot_right()
        elif moves == [1,1,0,0]:
            shoot_jump()
        elif moves == [0,0,1,0]:
            left()
        elif moves == [0,0,0,1]:
            right()
        elif moves == [1,0,0,0]:
            jump()
        elif moves == [0,1,0,0]:
            shoot()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
