import sys
import time
import keyboard
import pyautogui

pyautogui.FAILSAFE = False

while True:
	if keyboard.is_pressed('pause'):
		yol = 'C:/Py_SS/' + str(time.time()) + '.png'
		sscek = pyautogui.screenshot(yol)