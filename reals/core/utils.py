import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import OrderedDict, defaultdict

# from reals import f1_in, f2_out
from parser import excel_to_book
from schedule_classes import Calendar, Check


def advance_date(date, *args, **kwargs):
    assert isinstance(date, datetime)
    return date + relativedelta(**kwargs)


def advance_date_now(*args, **kwargs):
    return datetime.now() + relativedelta(**kwargs)


if __name__ == '__main__':
    # book = excel_to_book(f1_in)
    # book_to_calendar(book)
    # aircraft_info = book_to_aircraft_info(book)
    # for _ in aircraft_info:
    #     print(_)

    date = advance_date_now(days=2)

    # print(advance_date_now(days=1, weeks=1, months=1, years=1))
