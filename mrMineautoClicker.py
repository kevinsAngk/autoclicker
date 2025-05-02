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
        time.sleep(0.2)
        pydirectinput.keyDown('shift')
        time.sleep(0.2)
        click(1500,585)
        time.sleep(0.2)
        click(1500,585)
        time.sleep(0.2)
        pydirectinput.keyUp('shift')
        time.sleep(0.2)
    
    
def sell_material():
    c =0
    for c in range (3):
        pyautogui.press('s')
        time.sleep(0.5)
        pydirectinput.doubleClick(620,750)#press Sell
        time.sleep(0.5)

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
    pydirectinput.doubleClick(1060,890)
    time.sleep(0.8)
    pydirectinput.doubleClick(1000,750)
    time.sleep(0.8)
    pydirectinput.doubleClick(777,675)
    time.sleep(0.8)

def superminer():
    click(1830,290)
    time.sleep(0.8)
    click(1260,280)
    time.sleep(0.8)
    click(830,735)
    time.sleep(0.8)
    click(767,756)
    time.sleep(0.3)
    click(1200,175)
    time.sleep(0.8)
    click(1400,225)
    time.sleep(0.8)

def tradingPostStuff():
    click(850,600)
    time.sleep(0.8)
    click(1090,475)
    time.sleep(0.8)
    click(1098,545)
    click(950,700)
    time.sleep(0.3)

def tradingPost():
    click(1830,350)
    time.sleep(0.8)
    tradingPostStuff()
    click(1830,650)
    time.sleep(0.8)
    tradingPostStuff()
    click(1830,750)
    time.sleep(0.8)
    tradingPostStuff()
    
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
    pyautogui.press("b")
    time.sleep(0.4)
    click(802,490)
    time.sleep(0.3)
    click(802,490)
    time.sleep(0.5)
    click(1100,730)
    time.sleep(0.3)
    click(1100,730)
    time.sleep(0.3)
    pyautogui.press('esc')
    time.sleep(0.3)
    superminer()
    tradingPost()
    if checkReactorColour():
        click(1830,710)
        time.sleep(0.5)
        click(1000,500)
        time.sleep(0.5)
        click(1000,500)
        time.sleep(0.5)
        # click(1830,710)
        # time.sleep(0.3)
        reactorRechage()
        time.sleep(0.3)
        pydirectinput.keyDown('shift')
        time.sleep(0.3)
        for p in range (28):
            click(595,575)
        pydirectinput.keyUp('shift')
        time.sleep(0.3)
    
# running = False 

# def toggle_clicker():
#     """Toggle the auto clicker on/off."""
#     global running
#     running = not running
#     print(f"Auto clicker {'started' if running else 'stopped'}.")
    
# keyboard.add_hotkey("F6", toggle_clicker)  # Press F6 to toggle

def main(num,x):
    # toggle_clicker()
    # keyboard.add_hotkey("F6", toggle_clicker)
    if num == 1:
        while keyboard.is_pressed('z') == False:
            main_body(x)
    else :
        main_body()

main(1,1)
