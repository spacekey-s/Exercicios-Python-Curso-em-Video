import pyautogui as pat
import time as tp
import pyperclip

tp.sleep(3)
pat.press("win")
tp.sleep(2)
pat.typewrite("TikTok", interval=0.5)
tp.sleep(1)
pat.press("enter")
tp.sleep(20)
pat.click(111, 346, duration=1)
tp.sleep(5)
pat.click(454, 345, duration=1)
tp.sleep(5)

for loop in range(50):

    pat.click(1608, 997, duration=1)
    tp.sleep(1)
    pyperclip.copy("Independente do vídeo, Jesus está Voltando ! Acredite !")
    tp.sleep(1)
    pat.hotkey("ctrl", "v")
    tp.sleep(1)
    pat.press("Enter")
    tp.sleep(2)
    pat.click(798, 549, duration=1);tp.sleep(1)
    pat.hotkey("down")
    tp.sleep(5)
