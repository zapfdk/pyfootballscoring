import threading
from datetime import timedelta

class GameClock:
    def __init__(self, quarter_length):
        self.quarter_length = quarter_length
        self.running = False
        self.remaining_time = timedelta(minutes=quarter_length)

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def toggle(self):
        self.running = not self.running

    
    