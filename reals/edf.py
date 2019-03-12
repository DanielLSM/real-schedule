import numpy

from reals import f1_in, f2_out
from reals.parser import excel_to_book
from reals.utils import book_to_calendar, book_to_aircraft_info


class SchedulerEDF:
    """ Currently for C-Checks only """

    def __init__(self, *args, **kwargs):
        self.book = excel_to_book(f1_in)
        self.calendar = book_to_calendar(self.book)
        self.aircraft_info = book_to_aircraft_info(self.book)


if __name__ == '__main__':
    pass