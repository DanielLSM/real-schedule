import numpy
import pandas


class Task:

    def __init__(self, *args, **kwargs):
        self.name = 0

        self.C_previous_code = None
        self.C_max = None  #total numbers of c check in  c check cycle
        # actual variables
        self.DY_C = 0  #callendary days since previous C check
        self.FH_C = 0  #flight hours since previous C check
        self.FC_C = 0  #flight hours since previous C check

        # Intervals
        self.DY_C_interval = 0
        self.FH_C_interval = 0
        self.FC_C_interval = 0

        self.C_previous_start = 0
        self.C_previous_end = 0


class Callendar:

    def __init__(self, *args, **kwargs):
        self.start_date = None
        self.end_date = None

    def render(self):
        pass  #something something tkinter?
