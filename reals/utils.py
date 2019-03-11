import pandas
from collections import OrderedDict, defaultdict

from reals import f1_in, f2_out
from reals.common import Task, Callendar
from reals.parser import excel_to_book


def book_to_calendar(file_in: str):
    #currently only C_Checks
    #decompose book into a couple of sheets, use this sheets to restrict
    # the callendar as much as possible
    book = excel_to_book(f1_in)
    C_not_allowed = book['C_not_allowed']

    pass


def book_to_tasks():
    # will only consider C checks for now
    pass


if __name__ == '__main__':
    pass