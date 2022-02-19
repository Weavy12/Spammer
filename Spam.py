
#import pyautogui
import pyautogui, time
time.sleep(5)
# You have 5 seconds time to prepare yourself
f = open("beemovie.gay", 'r')
# You can change it to whatever you feel like. Doesn't have to be the beemovie script
for word in f:
    pyautogui.typewrite(word)
    time.sleep(0.5)
    # Used time.sleep so discord wont crash. If it still crashes for you put it on 1 second.
    pyautogui.press("enter")