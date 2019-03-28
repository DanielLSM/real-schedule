import pandas as pd
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import OrderedDict, defaultdict

from schedule_classes import Calendar, Check


def advance_date(date, *args, **kwargs):
    assert isinstance(date, datetime)
    return date + relativedelta(**kwargs)


def advance_date_now(*args, **kwargs):
    return datetime.now() + relativedelta(**kwargs)

def dates_between(date_start,date_end):
    assert date_end > date_start, "end date before start_date"
    delta = date_end - date_start
    return date.days

if __name__ == '__main__':
    # book = excel_to_book(f1_in)
    # book_to_calendar(book)
    # aircraft_info = book_to_aircraft_info(book)
    # for _ in aircraft_info:
    #     print(_)

    date = advance_date_now(days=2)

    # print(advance_date_now(days=1, weeks=1, months=1, years=1))
