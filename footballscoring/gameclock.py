import threading
from datetime import timedelta, datetime
from apscheduler.schedulers.background import BackgroundScheduler

from footballscoring.gameconfig import GameConfig
from footballscoring.definitions import Constraints

class GameClock:
    """Handles game clock, can be started, stopped, resetted, resumed and set to a certain time. 

    Args: 
        quarter_length (int): Length of a quarter in minutes.
        interval_ms (int): Specifies the interval in milliseconds, in which the clock should be updated.
    """
    def __init__(self, quarter_length, interval_ms=10):
        if Constraints.check_constraint("quarter_length", quarter_length):
            self.quarter_length = quarter_length
        self.running = False
        self.remaining_time = timedelta(minutes=quarter_length)
        self.previous_update_time = None
        self.interval_ms = interval_ms

        self.scheduler = BackgroundScheduler()

    def change_quarter_length(self, quarter_length):
        """Changes the quarter length.

        Args:
            quarter_length (int): Length of a quarter in minutes.
        Returns: 
            None
        """
        if Constraints.check_constraint("quarter_length", quarter_length):
            self.quarter_length = quarter_length

    def reset_clock(self, stop_clock=True):
        """Resets clock to quarter length.

        Args:
            stop_clock (bool): Specify whether the clock should be stopped or immediately resumed, defaults to True.
        Returns:
            None
        """
        self.remaining_time = timedelta(minutes=self.quarter_length)
        if stop_clock:
            self.running = False

    def set_clock(self, minutes, seconds, stop_clock=True):
        """Sets clock to a certain time.

        Args: 
            minutes (int): Minutes of the time
            seconds (int): Seconds of the time
            stop_clock (int): Specify whether clock should be stopped after setting the clock, defaults to True.
        Returns:
            None
        """
        self.remaining_time = timedelta(minutes=minutes, seconds=seconds)
        if stop_clock:
            self.running = False

    def start(self):
        """Starts the clock.

        Args:
            None
        Returns:
            None
        """
        self.running = True
        self.previous_update_time = datetime.now()
        self.scheduler.add_job(self.process_clock, 'interval', seconds=self.interval_ms/1000)
        self.scheduler.start()

    def stop(self):
        """Stops the clock.

        Args: 
            None
        Returns:
            None        
        """
        self.running = False

    def toggle(self):
        """Toggles the current running status of the clock.

        Args:
            None
        Returns:
            None
        """
        self.running = not self.running

    def process_clock(self):
        """Callback function for the background scheduler. If clock is set to running, counts down time passed since last iteration.

        Args:
            None
        Returns:
            None
        """
        if self.running:
            new_remaining_time = self.remaining_time - (datetime.now() - self.previous_update_time)
            if new_remaining_time < timedelta():
                self.remaining_time = timedelta()
                self.running = False
            else:
                self.remaining_time = new_remaining_time
        self.previous_update_time = datetime.now()
    
    