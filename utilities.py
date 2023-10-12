#Spinner 

import itertools
import threading
import time

class Spinner:
    def __init__(self, message):
        self.spinner_chars = itertools.cycle(['-', '/', '|', '\\'])
        self.is_active = False
        self.message = message

    def __enter__(self):
        self.is_active = True
        self.spinner_thread = threading.Thread(target=self.spin)
        self.spinner_thread.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_active = False
        self.spinner_thread.join()

    def spin(self):
        while self.is_active:
            print(f"\r{next(self.spinner_chars)} {self.message}", end='')
            time.sleep(0.1)