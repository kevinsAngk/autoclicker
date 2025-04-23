from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from pyautogui import *
import time
import win32api, win32con
#pyautogui.displayMousePosition()

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.25)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.10)