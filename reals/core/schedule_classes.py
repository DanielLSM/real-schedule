import numpy
import pandas as pd
from collections import OrderedDict, defaultdict

from reals.core.resources import f1_in, f2_out
from reals.core.parser import book_to_kwargs_MPO
from reals.core.utils import get_calendar, advance_date


class Calendar:
    def __init__(self, *args, **kwargs):
        self.time_type = kwargs['time_type']
        self.start_date = kwargs['start_date']
        self.end_date = kwargs['end_date']
        self.a_type = kwargs['a-type']
        self.c_type = kwargs['c-type']
        self.public_holidays = kwargs['all']
        self.calendar = get_calendar(
            self.start_date, self.end_date, type='days')

        import ipdb
        ipdb.set_trace()

    def restrict_calendar(self, restrict_list):
        pass

    def plan(self, time_window):
        pass

    def reset_calendar(self):
        pass

    def render(self):
        pass  # something something tkinter?


class Fleet:
    def __init__(self, *args, **kwargs):
        self.aircraft_info = kwargs


# this should be an abc abstract class
class FleetManagerBase:
    def __init__(self, *args, **kwargs):

        self.calendar = Calendar(**kwargs['restrictions'])
        self.fleet = Fleet(**kwargs['aircraft_info'])


if __name__ == '__main__':
    from reals.core.parser import excel_to_book
    try:
        book = excel_to_book(f1_in)
    except Exception as e:
        print('you messed up')
        raise e

    kwargs = book_to_kwargs_MPO(book)
    fmb = FleetManagerBase(**kwargs)
