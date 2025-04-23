from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pyautogui import *
import time
import pyautogui
import keyboard 
import win32api, win32con
import pydirectinput

#pyautogui.displayMousePosition()

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.25)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.25)

def clickVeryTop():
    for a in range(2):
        pydirectinput.doubleClick(100,200)#click very top
        time.sleep(0.25)

def compressToEthernalChest():
    for n in range(11):
        click(850,620) #compress to ethernal


def compresssToGoldchest():
    for i in range (11):
        click(610,630)#compress to gold

def checkCollectorColor():
    x_coord, y_coord = 258, 710
    watch_duration = 1.1  # seconds
    check_interval = 0.05  # check every 50ms 

    start_time = time.time()
    initial_color = 225, 235, 221

    while time.time() - start_time < watch_duration:
        current_color = pyautogui.pixel(x_coord, y_coord)
        if current_color != initial_color:
            return True  # Color changed during watch time
        time.sleep(check_interval)

    return False

def colector(y):
    num=y
    pydirectinput.doubleClick(250,750)#click chest colector
    time.sleep(0.3)
    click(850,750)# click colect chest
    time.sleep(0.3)
    OpenChest()
    time.sleep(0.3)
    if num==1:
        compressToEthernalChest()
    compresssToGoldchest()
    # click(600,560)# open basic chest
    time.sleep(0.5)
    pydirectinput.doubleClick(850,750)# click colect chest
    time.sleep(0.5)
    
    pydirectinput.doubleClick(1400,280)# close colector
    time.sleep(0.5)

def OpenChest():
    b = 0
    for b in range (3):
        # pydirectinput.press('space')
        # time.sleep(0.4)
        pydirectinput.keyDown('shift')
        time.sleep(0.3)
        click(600,565)
        pydirectinput.keyUp('shift')
        time.sleep(0.3)

def sell_material():
    c =0
    for c in range (3):
        pyautogui.press('s')
        time.sleep(0.3)
        pydirectinput.doubleClick(620,750)#press Sell
        time.sleep(0.35)

def checkReactorColour():
    x_coord, y_coord = 1815, 697
    watch_duration = 1.1  # seconds
    check_interval = 0.05  # check every 50ms 

    start_time = time.time()
    initial_color = (  0, 255,  0)

    while time.time() - start_time < watch_duration:
        current_color = pyautogui.pixel(x_coord, y_coord)
        if current_color != initial_color:
            return True  # Color changed during watch time
        time.sleep(check_interval)

    return False

def reactorRechage():
    click(1060,890)
    click(1000,750)
    click(777,675)

def main_body(x):
    clickVeryTop()
    if checkCollectorColor():
        colector(x)
        sell_material()
        # time.sleep(0.5)
        click(1400,280)# close colector
        time.sleep(0.3)
        click(770,645)
        time.sleep(0.3)
        click(770,645)
        time.sleep(0.3)
        pyautogui.press("b")
        time.sleep(0.4)
        click(802,490)
        click(802,490)
        pyautogui.press('esc')
        time.sleep(0.3)
    if checkReactorColour():
        pyautogui.press("r")
        reactorRechage()
        time.sleep(0.3)
        pydirectinput.keyDown('shift')
        time.sleep(0.3)
        for p in range (28):
            click(595,575)
        pydirectinput.keyUp('shift')
        time.sleep(0.3)
            
def main(num, x):
    if num == 1:
        print("Running... Press 'z' to activate, 'esc' to exit.")
        while True:
            if keyboard.is_pressed('esc'):
                print("Exiting script...")
                break
            if not keyboard.is_pressed('z'):
                main_body(x)
    else:
        main_body(x)


main(1,1)
