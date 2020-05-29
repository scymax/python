from pyautogui import *
import pyautogui as pg
import time
import keyboard
import random
import win32api, win32con

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
                   (r in range(200,230) and (g in range(70,90) and                                            
                   (b in range(90,110))))):
                pg.click(x+750,y+290)
                pg.click(1165, 360)
                time.sleep(0.05)
                pg.click(880, 370)
                pg.click(1150, 940)
                pg.click(1200, 720)
                pg.click(880, 440)
                pg.click(1150, 940)
                pg.click(1200, 720)
                pg.click(830, 950)
                pg.click(920, 950)
                pg.click(1010, 950)
                pg.click(1100, 950)
                time.sleep(2)
                break
