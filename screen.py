import cv2
import numpy as np
import settings
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication
import sys

path = settings.path
path2 = settings.path2
windowTile = settings.windowTile
hwnd = settings.hwnd


def find_btn(tz, num):
    img = cv2.imread(tz, 0)
    if num == 1:
        template = cv2.imread('startBtn.png', 0)
    elif num == 2:
        template = cv2.imread('start_bl.png', 0)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = settings.threshold
    gps = []

    coordinate = np.where(res >= threshold)  #
    for pt in zip(*coordinate[::-1]):  # *号表示可选参数
        gps.append(pt)

    if len(gps) > 1:
        print("More than 1 start button found!")
        return gps[0]

    elif len(gps) == 1:
        return gps[0]

    else:
        print("Unable to find start button!")
        return -1


def screen_monitor():
    # hwnd = win32gui.FindWindow(None, "Command Prompt")
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save(path2)


def screenshot():
    img = ImageGrab.grab()
    img.save(path)
