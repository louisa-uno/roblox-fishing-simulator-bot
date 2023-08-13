# Import necessary libraries
# Notwendige Bibliotheken importieren
from pydoc import cli
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pydirectinput


# Function to simulate a mouse click at given coordinates
# Funktion, um einen Mausklick an gegebenen Koordinaten zu simulieren
def click(x, y):
	win32api.SetCursorPos((x, y))
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Function to simulate a safe mouse click using pydirectinput
# Funktion, um einen sicheren Mausklick mit pydirectinput zu simulieren
def safety_click(x, y):
	pydirectinput.moveTo(x, y)
	time.sleep(random.uniform(0.01, 0.05))
	pydirectinput.click()


# Function to simulate a double mouse click at given coordinates
# Funktion, um einen Doppelklick an gegebenen Koordinaten zu simulieren
def double_click(x, y):
	click(x, y)
	time.sleep(random.uniform(0.02, 0.025))
	click(x, y)


# Function to get a counter value
# Funktion, um einen Zählerwert zu erhalten
def get_counter():
	counter = 150
	return counter


# Function to check for air bubbles on the screen
# Funktion, um nach Luftblasen auf dem Bildschirm zu suchen
def check_air_bubbles_on_screen():
	s = pyautogui.screenshot()
	for x in range(770, 1160):
		for y in range(350, 730):
			colorcode = (68, 252, 234)  # Blue bubbles / Blaue Blasen
			tempvar = False
			for x2 in range(5):
				if s.getpixel((x + x2, y)) == colorcode:
					tempvar = True
				else:
					tempvar = False
					break
			if tempvar is True:
				return True


# Function to simulate a random throw click
# Funktion, um einen zufälligen Wurfklick zu simulieren
def click_random_throw():
	x, y = random.randint(960, 970), random.randint(520, 530)
	win32api.SetCursorPos((x, y))
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Function to simulate a double random throw click
# Funktion, um einen doppelten zufälligen Wurfklick zu simulieren
def double_click_random_throw():
	click_random_throw()
	time.sleep(random.uniform(0.02, 0.025))
	click_random_throw()


# Initialize counters and flags
# Zähler und Flags initialisieren
counter = 0
fish_counter = 0
fish_found = False

# Main loop to check for fish and bubbles until 'q' is pressed
# Hauptloop, um nach Fischen und Blasen zu suchen, bis 'q' gedrückt wird
while keyboard.is_pressed('q') == False:
	# Check if fish is found
	# Überprüfen, ob ein Fisch gefunden wurde
	if pyautogui.pixel(847, 820)[0] == 255 or pyautogui.pixel(860,
	                                                          800)[0] == 255:
		# Reel in the fish
		# Den Fisch einholen
		click_random_throw()
		counter = get_counter()
		fish_found = True
	# Increase fish counter if found
	# Fischzähler erhöhen, wenn gefunden
	if fish_found == True:
		if pyautogui.pixel(830, 800) != (83, 250, 83):
			fish_counter += 1
			print('Fische gefangen: ' + str(fish_counter))
			fish_found = False
			double_click_random_throw()
	# If fish not found, check for air bubbles
	# Wenn kein Fisch gefunden wurde, nach Luftblasen suchen
	if fish_found == False:
		if check_air_bubbles_on_screen() == True:
			# Reel in the fish
			# Den Fisch einholen
			click_random_throw()
			counter = get_counter()
			fish_found = True
	if counter == 0:
		# Cast or reel in the fishing rod
		# Angel auswerfen oder einholen
		double_click_random_throw()
		counter = get_counter()
	# If inventory is full, sell
	# Wenn das Inventar voll ist, verkaufen
	if fish_counter == 2000:
		print('Inventar voll, verkaufe...')
		exit()
	counter -= 1
	time.sleep(0.025)
