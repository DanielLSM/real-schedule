import pandas as pd
from datetime import datetime, timedelta
from collections import OrderedDict, defaultdict

from reals import f1_in, f2_out
from reals.common import Check, Calendar
from reals.parser import excel_to_book


def book_to_calendar(book: dict):
    #currently only C_Checks
    #decompose book into a couple of sheets, use this sheets to restrict
    # the calendar as much as possible
    # a calendar is an ordered dict of days (each key is a date), within each day there are several
    # keys, main keys are:
    # 1)
    # 2)
    try:
        c_not_allowed = book['C_Not_Allowed']
        public_holidays = book['Public_Holidays']
        c_peak = book['C_Peak']
        additional = book['Additional']
        additional.set_index('Begin Year', inplace=True)
        additional = additional.T
    except Exception as e:
        print(e)
        raise e
    calendar_kwargs = {}
    start_date = pd.to_datetime(additional['Begin Day'][2017])
    calendar_kwargs['start_date'] = start_date
    calendar_kwargs['total_years'] = additional['Total Years'][2017]

    import ipdb
    ipdb.set_trace()
    calendar = Calendar()
    return calendar


def book_to_aircraft_info(book: dict):
    #for now we only have a master key of C-Checks
    c_inital = book['C_Initial']
    aircraft_info = OrderedDict()
    for _ in range(len(c_inital)):
        aircraft_id = c_inital['Aircraft ID'][_]
        aircraft_info[aircraft_id] = {}
        for key in c_inital.keys():
            if key is not 'Aitcraft_ID':
                aircraft_info[aircraft_id][key] = c_inital[key][_]
    return aircraft_info


def book_to_tasks(book: dict):
    pass


def advance_date(self, date, *args):
    return date.now() + timedelta(*args)


if __name__ == '__main__':
    # book = excel_to_book(f1_in)
    # book_to_calendar(book)
    # aircraft_info = book_to_aircraft_info(book)
    # for _ in aircraft_info:
    #     print(_)
