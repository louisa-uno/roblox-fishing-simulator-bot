from pydoc import cli
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pydirectinput


def click(x, y):
	win32api.SetCursorPos((x, y))
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def safety_click(x, y):
	pydirectinput.moveTo(x, y)
	time.sleep(random.uniform(0.01, 0.05))
	pydirectinput.click()


def double_click(x, y):
	click(x, y)
	time.sleep(random.uniform(0.02, 0.025))
	click(x, y)


def get_counter():
	# counter = random.randint(default_counter,
	#                          default_counter + default_counter_variation)
	counter = 150
	return counter


def check_air_bubbles_on_screen():
	s = pyautogui.screenshot()
	for x in range(770, 1160):
		for y in range(350, 730):
			colorcode = (68, 252, 234)  # Blaue Blasen
			# colorcode = (255, 131, 8):  # Orange Blasen
			tempvar = False
			for x2 in range(5):
				if s.getpixel((x + x2, y)) == colorcode:
					tempvar = True
				else:
					tempvar = False
					break
			if tempvar is True:
				return True


def click_random_throw():
	# x, y = random.randint(400, 1500), random.randint(200, 700)
	x, y = random.randint(960, 970), random.randint(520, 530)
	win32api.SetCursorPos((x, y))
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def double_click_random_throw():
	click_random_throw()
	time.sleep(random.uniform(0.02, 0.025))
	click_random_throw()


counter = 0
fish_counter = 0
fish_found = False

while keyboard.is_pressed('q') == False:
	# Check ob Fisch gefunden
	if pyautogui.pixel(847, 820)[0] == 255 or pyautogui.pixel(860,
	                                                          800)[0] == 255:
		# Fisch einholen
		click_random_throw()
		counter = get_counter()
		fish_found = True
	# Fischcounter erhöhen, wenn gefunden
	if fish_found == True:
		if pyautogui.pixel(830, 800) != (83, 250, 83):
			fish_counter += 1
			print('Fische gefangen: ' + str(fish_counter))
			fish_found = False
			double_click_random_throw()
	# Wenn Fisch noch nicht gefunden nach Luftblasen suchen
	if fish_found == False:
		if check_air_bubbles_on_screen() == True:
			# Fisch einholen
			click_random_throw()
			counter = get_counter()
			fish_found = True
	if counter == 0:
		# Angel neu auswerfen/einholen
		double_click_random_throw()
		counter = get_counter()
	# Wenn Inventar voll verkaufen
	if fish_counter == 2000:
		print('Inventar voll, verkaufe...')
		exit()
	counter -= 1
	time.sleep(0.025)
