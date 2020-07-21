import screen
import settings
import time
import random
import events
import math
import pyautogui as agui


class GameScript:
    agui.FAILSAFE = True

    def __init__(self):
        '''
        tl┏------┐tr
          |      |
          |      |
        bl└------┘br
        '''
        self.tlx = 0
        self.tly = 0
        self.brx = 0
        self.bry = 0
        self.path = settings.path
        self.path2 = settings.path2

        self.timer = 0
        self.event_num = 0
        self.pre_event_num = 0

    def initialise(self):
        time.sleep(5)
        screen.screenshot()
        start_cor = screen.find_btn(self.path, 1)  # Coordinate of start button
        end_cor = screen.find_btn(self.path, 2)
        print(str(start_cor) + '-->' + str(end_cor))

        '''
        Calculate the coordinate range of the start button
        '''
        startStr = str(start_cor).replace(' ', '')
        startStr = startStr.replace('(', '')
        startStr = startStr.replace(')', '')
        self.tlx = int(startStr.split(',')[0])
        self.tly = int(startStr.split(',')[1])

        endStr = str(end_cor).replace(' ', '')
        endStr = endStr.replace('(', '')
        endStr = endStr.replace(')', '')
        self.brx = int(endStr.split(',')[0]) * 2 - self.tlx
        self.bry = int(endStr.split(',')[1]) * 2 - self.tly

    '''

    '''

    def move_to_random_cor(self):
        r_time = random.uniform(settings.mouse_movement_duration_min, settings.mouse_movement_duration_max)
        r_x = random.randint(self.tlx, self.brx)
        r_y = random.randint(self.tly, self.bry)
        agui.moveTo(r_x, r_y, r_time, agui.easeInBounce)

    def start_game(self):
        click_times = random.randint(settings.click_startBtn_times_min, settings.click_startBtn_times_max)
        self.move_to_random_cor()
        for i in range(0, click_times):
            agui.click(agui.position())
            self.random_move()
            time.sleep(random.uniform(settings.mouse_click_duration_min, settings.mouse_click_duration_max))
        move_up = -random.randint(0, math.floor(
            self.bry * 3 / 4))  # After clicking start button, the mouse moves up random distance
        move_left = - random.randint(0, math.floor(self.brx / 50))
        r_time = random.uniform(settings.mouse_movement_duration_min, settings.mouse_movement_duration_max)
        agui.moveRel(move_left, move_up, r_time, agui.easeInBounce)

    def end_game(self):
        click_times = random.randint(settings.click_when_finish_times_min, settings.click_when_finish_times_max)
        for i in range(0, click_times):
            agui.click(agui.position())
            self.random_move()
            time.sleep(random.uniform(settings.mouse_click_duration_min, settings.mouse_click_duration_max))

    # Only move to left, and a little up and down, in case that pointer goes out of bound
    def random_move(self):
        r_l = -random.randint(0, math.floor(self.brx / 60))
        r_ud = math.floor(math.floor(self.bry / 50) - random.randint(0, math.floor(self.bry / 25)))
        agui.moveRel(r_l, r_ud, 0.15, agui.easeInQuad)

    def main_script(self):
        eve = events.Events()
        print("start main script")
        while True:
            if self.timer >= settings.timeout:
                print("Time out, restart game!")
                self.start_game()
            screen.screen_monitor()
            event_num = eve.find_case_num(path=self.path2)
            if event_num == 1:
                if self.pre_event_num != 1:
                    self.timer = 0
                    self.start_game()
            elif event_num == 2:
                if self.pre_event_num != 2:
                    self.timer = 0
                    self.end_game()
            elif event_num == 3:
                if self.pre_event_num != 3:
                    self.timer = 0
                    self.end_game()
            self.pre_event_num = self.event_num
            time.sleep(1)
            self.timer += 1
