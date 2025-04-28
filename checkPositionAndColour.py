import pyautogui


pyautogui.displayMousePosition()
x, y = 850, 750  # Replace with your coordinates
color = pyautogui.pixel(x, y)
print(f"Color at ({x}, {y}): {color}")  # Output will be (R, G, B)


