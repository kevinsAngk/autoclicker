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
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    pydirectinput.keyDown('shift')
    time.sleep(0.2)
    click(190, 615)
    time.sleep(0.2)
    click(190, 615)
    time.sleep(0.02)
    click(610, 615)
    time.sleep(0.02)
    pydirectinput.keyUp('shift')
    time.sleep(0.02)
    pyautogui.press('g')
    time.sleep(0.02)
    pydirectinput.keyDown('shift')
    time.sleep(0.02)
    pydirectinput.doubleClick(745, 615)
    time.sleep(0.02)
    pydirectinput.doubleClick(745, 615)
    time.sleep(0.02)
    pydirectinput.doubleClick(745, 615)
    time.sleep(0.02)
    pydirectinput.doubleClick(745, 615)
    time.sleep(0.04)
    pydirectinput.doubleClick(745, 615)
    time.sleep(0.02)
    pydirectinput.keyUp('shift')
    time.sleep(0.04)
    pyautogui.press('s')
    time.sleep(0.4)
    pyautogui.press('s')
    time.sleep(0.4)
    pydirectinput.doubleClick(623, 762)
    time.sleep(0.04)
    pyautogui.press('s')
    time.sleep(0.4)
    pydirectinput.doubleClick(623, 762)
    time.sleep(0.04)
    pyautogui.press('esc')
    time.sleep(0.04)
    #  ChestColector
    # press up
    pydirectinput.doubleClick(114, 198)
    time.sleep(0.04)
    # press colector
    click(244, 761)
    time.sleep(0.04)
    # press open basic chest
    # pydirectinput.doubleClick(625, 581)
    # time.sleep(0.04)
    # press compress
    pydirectinput.doubleClick(955, 690)
    time.sleep(0.04)
    pyautogui.press('esc')
    time.sleep(0.04)
    pydirectinput.press('space')
    time.sleep(0.04)