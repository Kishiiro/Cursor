import sys
import random
import time
import pyautogui as screen
import keyboard
while True:
    if keyboard.is_pressed('Esc'):
        sys.exit()
    x= random.randint(600,700)
    y=random.randint(200,600)
    screen.moveTo(x,y,0.5)
    time.sleep(3)

   
    

 
