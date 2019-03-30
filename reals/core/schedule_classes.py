import numpy
import pandas as pd
from collections import OrderedDict, defaultdict
# from parser import book_to_kwargs_MPO


class Calendar:

    def __init__(self, *args, **kwargs):
        self.start_date = kwargs['start_date']
        self.end_date = kwargs['end_date']
        self.total_years = kwargs['total_years']
        #all the not allowed days
        self.not_allowed = kwargs['not_allowed']
        self.calendar = self._setup_calendar()

    def advance_to_date(self, date):
        pass

    def plan_days(self, days):
        pass

    def plan_weeks(self, weeks):
        pass

    def plan_months(self, months):
        pass

    def plan_years(self, years):
        pass

    def render(self):
        pass  #something something tkinter?

    def _setup_calendar(self):
        calendar = OrderedDict()
        calendar[self.start_date] = {}

        return calendar


class Check:

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