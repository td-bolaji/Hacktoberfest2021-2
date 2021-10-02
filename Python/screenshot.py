import pyautogui
import random
number = random.randint(0, 1000)
number = str(number)
screenshot = pyautogui.screenshot()
screenshot.save(number + "screenshot.png")                                                 
