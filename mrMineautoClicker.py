from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pyautogui import *
import time
import threading
import pynput    
import pyautogui
import keyboard 
import random
import win32api, win32con
import pydirectinput


#pyautogui.displayMousePosition()
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.25)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    

def compressToEthernalChest():
    n = 0
    for n in range(11):
        click(850,620) #compress to ethernal
        time.sleep(0.25)

def compresssToGoldchest():
    i = 0
    for i in range (11):
        click(610,630)#compress to gold
        time.sleep(0.25)
    


def colector(y):
    num=y
    for a in range(2):
        pydirectinput.doubleClick(100,200)#click very top
        time.sleep(0.25)
    time.sleep(0.25)
    pydirectinput.doubleClick(250,750)#click chest colector
    time.sleep(0.4)
    click(850,750)# click colect chest
    time.sleep(0.4)
    if num==1:
        compressToEthernalChest()
        compresssToGoldchest()
    else:
        compresssToGoldchest()
    # click(600,560)# open basic chest
    time.sleep(0.5)
    pydirectinput.doubleClick(850,750)# click colect chest
    time.sleep(0.5)
    pydirectinput.doubleClick(1400,280)# close colector
    time.sleep(0.5)
    
def collect_wild_chest():
    b = 0
    for b in range (4):
        pydirectinput.press('space')
        time.sleep(0.4)
        pydirectinput.keyDown('shift')
        time.sleep(0.3)
        click(1500,585)
        time.sleep(0.3)
        click(1500,585)
        time.sleep(0.3)
        pydirectinput.keyUp('shift')
        time.sleep(0.5)
    
    
def sell_material():
    c =0
    for c in range (3):
        pyautogui.press('s')
        time.sleep(0.5)
        pydirectinput.doubleClick(620,750)#press Sell
        time.sleep(0.5)


def main_body(x):
    colector(x)
    collect_wild_chest()
    sell_material()
    # time.sleep(0.5)
    click(1400,280)# close colector
    time.sleep(0.5)
    click(770,645)
    time.sleep(0.3)
    click(770,645)
    time.sleep(0.3)
    
running = False 

def toggle_clicker():
    """Toggle the auto clicker on/off."""
    global running
    running = not running
    print(f"Auto clicker {'started' if running else 'stopped'}.")
    
keyboard.add_hotkey("F6", toggle_clicker)  # Press F6 to toggle

def main(num,x):
    toggle_clicker()
    keyboard.add_hotkey("F6", toggle_clicker)
    if num == 1:
        while keyboard.is_pressed('z') == False:
            main_body(x)
    else :
        main_body()

main(1,1)
