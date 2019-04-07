import numpy
import pandas as pd
from collections import OrderedDict, defaultdict

from reals.core.resources import f1_in, f2_out
from reals.core.parser import book_to_kwargs_MPO
from reals.core.utils import advance_date, dates_between


def get_calendar(start_date, end_date, type='days'):
    n_days = dates_between(start_date, end_date, type='days')
    calendar = OrderedDict()
    for _ in range(n_days + 1):
        calendar[advance_date(start_date, days=_)] = {
            'allowed': {
                'public holidays': True,
                'a-type': True,
                'c-type': True
            },
            'resources': {
                'slots': {
                    'a-type': 1,
                    'c-type': 1
                }
            }
        }
    return calendar


class Calendar:
    def __init__(self, *args, **kwargs):
        self.time_type = kwargs['time_type']
        self.start_date = kwargs['start_date']
        self.end_date = kwargs['end_date']
        self.a_type = kwargs['a-type']
        self.c_type = kwargs['c-type']
        self.public_holidays = kwargs['all']

        print("#########################")
        print("INFO: setting up initial calendar")
        calendar = get_calendar(self.start_date, self.end_date, type='days')
        print("INFO: adding public holidays")
        calendar = self.restrict_calendar(
            calendar, self.public_holidays['time'], info='public holidays')

        print("INFO: adding a-type calendar restrictions")
        calendar = self.restrict_calendar(
            calendar, self.a_type['time'], info='a-type')

        print("INFO: adding c-type calendar restrictions")
        calendar = self.restrict_calendar(
            calendar, self.c_type['time'], info='c-type')

        print("INFO: adding a-type resources (slots)")
        calendar = self.add_resources(
            calendar, self.a_type['resources'], typek='slots', info='a-type')

        print("INFO: adding c-type resources (slots)")
        calendar = self.add_resources(
            calendar, self.c_type['resources'], typek='slots', info='a-type')

        print("#########################")
        self.calendar = calendar
        print("INFO: calendar complete!")

    @staticmethod
    def restrict_calendar(calendar, restrict_list, info='not allowed'):
        start_date = list(calendar.keys())[0]
        end_date = list(calendar.keys())[-1]

        for _ in restrict_list:
            if _ > start_date and _ < end_date:
                calendar[_]['allowed'][info] = False
        return calendar

    @staticmethod
    def add_resources(calendar, restrict_dict, typek='slots', info='a-type'):
        start_date = list(calendar.keys())[0]
        end_date = list(calendar.keys())[-1]

        for _ in restrict_dict[typek].keys():
            if _ > start_date and _ < end_date:
                calendar[_]['resources'][typek][info] += 1
        return calendar

    def plan(self, time_window):
        pass

    def reset_calendar(self):
        pass

    def render(self):
        pass  # something something tkinter?


class Fleet:
    def __init__(self, *args, **kwargs):

        self.aircraft_info = kwargs
        import ipdb
        ipdb.set_trace()


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
