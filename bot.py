# Import necessary libraries for automation, time management, and system interaction
from pydoc import cli  # Importing command-line interface utilities
from pyautogui import *  # Importing PyAutoGUI for automation of GUI interactions
import pyautogui  # Import PyAutoGUI for pixel color detection and mouse operations
import time  # Import time for adding delays
import keyboard  # Import keyboard for monitoring key presses
import random  # Import random for generating random values
import win32api, win32con  # Import win32api and win32con for low-level system control
import pydirectinput  # Import pydirectinput for safer and smoother input simulation
import math
import win32gui
import win32ui
# KC info
# monitorFishingPixel = 891, 877
# mouseClickCords = (971, 426)
# bagFullTextCords = (1055, 771)
# sellButtonCords = (1084, 356)
# sellEverthingCords = (1211, 492)
# KB info
# monitorFishingPixel = 1185, 1065
# sellButtonCords = (1433, 433)
# sellEverthingCords = (1710, 580)
# bagFullTextCords = (1163, 937)
fishingGaugeColor = (255, 255, 255)  # WHITE
fishingMeterColor = (83, 250, 83)  # GREEN
bubbleColor = (68, 252, 234)  # Define the RGB color code for air bubbles
monitorFishingPixel = 1185, 1065
mouseClickCords = (971, 426)
bagFullTextCords = (1055, 771)
bagFullTextColor = (253, 0, 97)  # RED
sellButtonCords = (1084, 356)
sellEverthingCords = (1211, 492)

sellGamepass = True  # CHANGE TO FALSE IF NO SELL GAMEPASS


# Function to simulate a mouse click at specific coordinates
def click(x, y):
    win32api.SetCursorPos((x, y))  # Move the cursor to the specified coordinates
    time.sleep(
        random.uniform(0.001, 0.005)
    )  # Add a small random delay for human-like behavior
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTDOWN, 0, 0
    )  # Simulate mouse left button press
    time.sleep(
        random.uniform(0.001, 0.005)
    )  # Add another delay before releasing the button
    win32api.mouse_event(
        win32con.MOUSEEVENTF_LEFTUP, 0, 0
    )  # Simulate mouse left button release


# Function to retrieve a counter value for controlling loop iterations
def get_counter():
    counter = 15  # Set the counter to a predefined value
    return counter  # Return the counter value


# Function to detect specific air bubbles on the screen based on their color
def capture_screen():
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    hwin = win32gui.GetDesktopWindow()
    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, screen_width, screen_height)
    memdc.SelectObject(bmp)

    memdc.BitBlt((0, 0), (screen_width, screen_height), srcdc, (0, 0), win32con.SRCCOPY)
    bits = bmp.GetBitmapBits(True)

    # Clean up resources
    memdc.DeleteDC()
    srcdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    return bits, screen_width, screen_height

def get_resolution_pyautogui():
    cur_width, cur_height = pyautogui.size()
    return cur_width, cur_height
class BubbleDetector:
    def __init__(self):
        self.last_detection_time = 0
        self.detection_cooldown = 2.0  # Cooldown in seconds

    def check_air_bubbles_on_screen(self):
        """Check for air bubbles with cooldown to prevent multiple detections"""
        current_time = time.time()
        if current_time - self.last_detection_time < self.detection_cooldown:
            return False

        try:
            bits, screen_width, screen_height = capture_screen()

            chunk_size = 50
            matches_found = False

            for y in range(0, screen_height - chunk_size, chunk_size):
                if matches_found:
                    break
                for x in range(0, screen_width - chunk_size, chunk_size):
                    matches = 0
                    for sample_y in range(y, y + chunk_size, 2):
                        for sample_x in range(x, x + chunk_size, 2):
                            pixel_offset = ((sample_y * screen_width + sample_x) * 4)
                            if pixel_offset + 2 >= len(bits):
                                continue

                            b = bits[pixel_offset]
                            g = bits[pixel_offset + 1]
                            r = bits[pixel_offset + 2]

                            if (abs(r - 68) < 2 and
                                abs(g - 252) < 2 and
                                abs(b - 234) < 2):
                                matches += 1

                            if matches >= 3:
                                self.last_detection_time = current_time
                                return True

            return False

        except Exception as e:
            print(f"Error checking bubbles: {e}")
            return False

def leftClick():
    time.sleep(random.uniform(0.001, 0.005))  # Pause for a short, randomized duration
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # Simulate mouse press
    time.sleep(random.uniform(0.001, 0.005))  # Pause for a short, randomized duration
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # Simulate mouse release


# Function to simulate a mouse click at random coordinates within a defined range
def click_random_throw():
    x, y = random.randint(mouseClickCords[0], mouseClickCords[0] + 10), random.randint(
        mouseClickCords[1], mouseClickCords[1] + 10
    )  # Generate random coordinates
    # x, y = random.randint(960, 970), random.randint(520, 530)  # Generate random coordinates
    win32api.SetCursorPos((x, y))  # Move the cursor to the random coordinates
    leftClick()


# Function to simulate a double mouse click at random coordinates within a defined range
def double_click_random_throw():
    click_random_throw()  # Perform the first random click
    time.sleep(random.uniform(0.02, 0.025))  # Add a short delay
    click_random_throw()  # Perform the second random click


def check_full_inv():
    if pyautogui.pixel(*bagFullTextCords) == bagFullTextColor:
        return True


def sell_inventory():
    keyboard.press("f")
    keyboard.release("f")
    time.sleep(0.10)
    win32api.SetCursorPos(sellButtonCords)
    time.sleep(0.10)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    leftClick()
    time.sleep(0.10)
    win32api.SetCursorPos(sellEverthingCords)
    time.sleep(0.10)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    leftClick()
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -20, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    time.sleep(1)
    leftClick()
    time.sleep(1)
    keyboard.press("f")
    keyboard.release("f")
    time.sleep(0.10)


def fishingBarCheck():
    # Number of pixels to check horizontally around monitorFishingPixel
    pixel_range = 3

    for offset in range(0, pixel_range + 1):  # Iterate from -5 to 5
        # Adjust x-coordinate of the pixel being checked
        x, y = monitorFishingPixel
        current_pixel = (x + offset, y)

        try:
            # Check if the pixel matches either color
            if (
                pyautogui.pixel(*current_pixel) == fishingMeterColor
                or pyautogui.pixel(*current_pixel) == fishingGaugeColor
            ):
                return True  # A match is found
        except Exception as e:
            print(f"Error checking pixel at {current_pixel}: {e}")

    return False  # No match found

def main():
		# Initialize counters and flags
	bubble_detector = BubbleDetector()
	counter = 0  # General counter for loop control
	fish_counter = 0  # Counter to track the number of fish caught
	fish_found = False  # Flag to indicate if a fish is currently detected

	# Main loop that continues until the 'q' key is pressed
	while keyboard.is_pressed("q") == False:
		# # Check if a fish is detected at specific screen coordinates
		# if pyautogui.pixel(847, 820)[0] == 255 or pyautogui.pixel(860, 800)[0] == 255:
		#     click_random_throw()  # Perform a random click to reel in the fish
		#     counter = get_counter()  # Reset the counter

		# Increment fish counter if a fish was detected
		if fish_found == True:
			print("Fish hooked! Reeling...")
			# while pyautogui.pixel(*monitorFishingPixel) == fishingMeterColor or pyautogui.pixel(*monitorFishingPixel) == fishingGaugeColor:
			while fishingBarCheck() == True:

				if pyautogui.pixel(*monitorFishingPixel) == fishingGaugeColor:
					print("Reeling Threshold hit! Pulling HARDER!!")
					double_click_random_throw()
				time.sleep(0.005)

			# Check if the pixel color at specific coordinates does not match the fishingbar colors
			if (
				pyautogui.pixel(*monitorFishingPixel) != fishingMeterColor
				or pyautogui.pixel(*monitorFishingPixel) != fishingGaugeColor
			):
				fish_counter += 1  # Increment the fish counter
				print("Fish caught: " + str(fish_counter))  # Log the number of fish caught
				fish_found = False  # Reset the fish detection flag
				print("RECASTING...")
				time.sleep(0.2)
				double_click_random_throw()  # Perform a double random throw to reset the fishing rod

		# If no fish is detected, check for air bubbles on the screen
		if fish_found == False:
			if bubble_detector.check_air_bubbles_on_screen() == True:
				print("Detected Bubbles. Attempting to reel.")
				click_random_throw()  # Perform a random click to reel in the fish
				counter = get_counter()  # Reset the counter
				fish_found = True  # Set the flag indicating a fish is found

		# If the counter reaches zero, perform a throw or reel-in action
		print("Waiting for Bubbles. Recasting in: ", counter)
		if counter == 0:
			time.sleep(0.1)
			keyboard.press("1")
			time.sleep(0.1)
			keyboard.release("1")
			time.sleep(0.1)
			keyboard.press("1")
			time.sleep(0.1)
			keyboard.release("1")
			time.sleep(0.3)
			double_click_random_throw()  # Perform a double random throw to reset the fishing rod
			counter = get_counter()  # Reset the counter

		# If the inventory is full, sell fish
		if check_full_inv() == True:
			if sellGamepass:
				print("Inventory full, selling...")  # Log the inventory status
				sell_inventory()
			else:
				print("Inventory full. Sell Gamepass is set to False.")
				print("Quitting Program.")
				exit()

		counter -= 1  # Decrement the counter on each loop iteration
		time.sleep(0.025)  # Add a small delay to reduce CPU usage
if __name__ == "__main__":
	main()