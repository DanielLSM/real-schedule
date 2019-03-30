import numpy
import pandas as pd
from collections import OrderedDict, defaultdict
# from parser import book_to_kwargs_MPO

from reals.core.resources import f1_in, f2_out
from reals.core.parser import book_to_kwargs_MPO


class Calendar:
    def __init__(self, *args, **kwargs):
        self.start_date = kwargs['start_date']
        self.end_date = kwargs['end_date']
        self.total_years = kwargs['total_years']
        # all the not allowed days
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
        pass  # something something tkinter?

    def _setup_calendar(self):
        calendar = OrderedDict()
        calendar[self.start_date] = {}

        return calendar


class Fleet:
    def __init__(self, *args, **kwargs):
        self.name = 0

        self.C_previous_code = None
        self.C_max = None  # numbers of c check in  c check cycle
        # actual variables
        self.DY_C = 0  # callendary days since previous C check
        self.FH_C = 0  # hours since previous C check
        self.FC_C = 0  # hours since previous C check

        # Intervals
        self.DY_C_interval = 0
        self.FH_C_interval = 0
        self.FC_C_interval = 0

        self.C_previous_start = 0
        self.C_previous_end = 0


# this should be an abc abstract class
class FleetManagerBase:
    def __init__(self, *args, **kwargs):
        self.fleet = Fleet(**kwargs['aircraft_info'])
        self.calendar = Calendar(**kwargs['calendar_restrictions'])


if __name__ == '__main__':
    from reals.core.parser import excel_to_book
    try:
        book = excel_to_book(f1_in)
    except Exception as e:
        print('you messed up')
        raise e

    kwargs = book_to_kwargs_MPO(book)
