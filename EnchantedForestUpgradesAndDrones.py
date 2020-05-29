from pyautogui import *
import pyautogui as pg
import time
import keyboard
import random
import win32api, win32con
#74, 108, 227
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pg.screenshot(region=(750,290,421,477))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if (
                   r == 221  and g == 85 and                                            
                   b == 102):
                pg.click(x+750,y+290)
                time.sleep(0.1)
                pg.click(1165, 360)
                break
