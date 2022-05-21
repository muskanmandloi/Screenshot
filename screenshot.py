import pyautogui
import time
image = pyautogui.screenshot()
time.sleep(5)
image.save("scrennshot.png")