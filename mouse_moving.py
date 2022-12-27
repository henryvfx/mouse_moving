import pyautogui as pag
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x,y,0.5)
    time.sleep(0.5)


# If you are having trouble exiting this program, quickly pull the mouse to the top left or right corner(s). This will enable the pag failsafe.
