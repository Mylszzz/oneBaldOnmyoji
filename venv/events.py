import cv2
import numpy as np
import settings


class Events:
    def __init__(self):
        self.template1 = cv2.imread('teamate_join.png', 0)  # Before start : click start button
        self.template2 = cv2.imread('finish1.png', 0)  # Finish battle, stage 1, click on screen
        self.template3 = cv2.imread('finish2.png', 0)  # Finish battle, stage 2, click on screen
        self.img_path = ""
        self.case_num = -1

    def find_case_num(self, path):
        self.img_path = path
        threshold = settings.threshold
        img = cv2.imread(self.img_path, 0)  # The image to be regonized

        gps = []
        res1 = cv2.matchTemplate(img, self.template1, cv2.TM_CCOEFF_NORMED)
        coordinate1 = np.where(res1 >= threshold)
        for pt in zip(*coordinate1[::-1]):
            gps.append(pt)
        if len(gps) >= 1:
            print('case 1: Teamate join, let\'s get started!')
            return 1

        res2 = cv2.matchTemplate(img, self.template2, cv2.TM_CCOEFF_NORMED)
        coordinate2 = np.where(res2 >= (threshold-0.1))
        for pt in zip(*coordinate2[::-1]):
            gps.append(pt)
        if len(gps) >= 1:
            print('case 2: Finish!')
            return 2

        res3 = cv2.matchTemplate(img, self.template3, cv2.TM_CCOEFF_NORMED)
        coordinate3 = np.where(res3 >= (threshold-0.1))
        for pt in zip(*coordinate3[::-1]):
            gps.append(pt)
        if len(gps) >= 1:
            print('case 3: Next go!')
            return 3

        return 0
