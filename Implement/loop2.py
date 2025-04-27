import pyautogui
import time
pyautogui.hotkey('winleft', 'q')
time.sleep(0.5)
pyautogui.typewrite("Whats")
pyautogui.press("Enter")
time.sleep(2.5)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("Varsha Ben")
pyautogui.press("tab")
pyautogui.press("Enter")
time.sleep(2)
count = 1
# a='pppp'
while count <= 500:
    if (count % 2 == 0):
        pyautogui.typewrite("%d. hi dudu" % (count))
    else:
        pyautogui.typewrite("%d. how are you" % (count))
    # pyautogui.typewrite(a)
    time.sleep(0.5)
    pyautogui.press("Enter")
    count += 1
    # a++

# while count <= 50:
#     pyautogui.typewrite("Neech")
#     time.sleep(0.5)
#     pyautogui.press("Enter")
#      count += 1
