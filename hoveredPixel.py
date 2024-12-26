import pyautogui
import keyboard
import time

# DEVELOPER USE ONLY
# USE TO GET PIXEL INFO (such as position and color) FROM MOUSE.

print("Move your mouse to the desired pixel position and wait...")
time.sleep(7)  # Gives you time to move the mouse

# Get the current mouse position
x, y = pyautogui.position()

# Get the color of the pixel under the mouse
while keyboard.is_pressed('q') == False:
    pixel_color = pyautogui.pixel(x, y)
    print(f"The mouse is at ({x}, {y}) and the pixel color is {pixel_color}")
    time.sleep(0.25)
