from PyQt5.QtWidgets import QApplication
import sys
import time


path = 'C:/Users/Samuel Shi/Desktop/resource/'
hwnd = 2426994
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
time.sleep(5)
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
for i in range(0, 100):
    img = screen.grabWindow(hwnd).toImage()
    path1 = path + str(i) + '.png'
    img.save(path1)
    print('saved:'+path1)
    time.sleep(0.5)
