import pandas as p
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
    calendar = Calendar()
    try:
        c_not_allowed = book['C_Not_Allowed']
        public_holidays = book['Public_Holidays']
        c_peak = book['C_Peak']
        additional = book['Additional']
    except e as Exception:
        print(e)
        print("problably some of these keys do not exist")
    return calendar


def book_to_aircraft_info(book: dict):
    #for now we only have a master key of C-Checks
    c_inital = book['C_Initial']
    # print(c_inital)


def book_to_tasks(book: dict):
    pass


if __name__ == '__main__':
    book = excel_to_book(f1_in)
    book_to_calendar(book)
    c_initial = book_to_aircraft_info(book)