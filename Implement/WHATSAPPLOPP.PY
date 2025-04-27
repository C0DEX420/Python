import pyautogui
import time
import random
pyautogui.hotkey('winleft', 'q')
time.sleep(0.5)
pyautogui.typewrite("Whats")
pyautogui.press("Enter")
time.sleep(2.5)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("Keshav2")
pyautogui.press("tab")
pyautogui.press("Enter")
time.sleep(2)
count = 1

gaali = ["hi bro"]
while count <= len("gaali")
    pyautogui.typewrite(random.choice(gaali))
    time.sleep(0.5)
    pyautogui.press("Enter")
    count += 1