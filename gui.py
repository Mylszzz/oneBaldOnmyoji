import tkinter
import script
import threading
import time


class OneBaldOnmyojiGui(object):

    ready = -1

    def __init__(self):
        self.root = tkinter.Tk()
        # Main window title
        self.root.title("One Bald Onmyoji --by Samuel Shi")
        # Create an input box
        self.ip_input = tkinter.Entry(self.root, width=50)
        # Create a information box
        self.info_box = tkinter.Listbox(self.root, width=50)
        # Create a button
        self.run_button = tkinter.Button(self.root, command=self.is_ready, text="Go!")

    def gui_arrange(self):
        self.ip_input.pack()
        self.info_box.pack()
        self.run_button.pack()

    def show_info(self, info):
        self.info_box.insert(0, info)

    def is_ready(self):
        global ready
        ready = 1
        self.show_info(info="Mission started!")
        time.sleep(0.3)
        t = threading.Thread(target=self.run_script, name='ScriptThread')
        print('thread %s is running...' % threading.current_thread().name)
        t.start()
        t.join()

    def run_script(self):
        print('thread %s is running...' % threading.current_thread().name)
        new_script = script.GameScript()
        new_script.initialise()
        new_script.main_script()

    def initialise():
        FL = OneBaldOnmyojiGui()
        FL.gui_arrange()
        tkinter.mainloop()
        pass
