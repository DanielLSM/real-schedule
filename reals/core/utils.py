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
    return delta.days

def dict_to_list(pandas_dict):
    pandas_list = []
    for value in pandas_dict.values():
        pandas_list.append(value)
    assert len(pandas_list)==len(list(pandas_dict.keys()))
    return pandas_list

def diff_time_list(sheet,type='days'):
    # in the future we would like to...... use types different than days
    sheet_keys =  list(sheet.keys())
    assert 'Begin' in sheet_keys and 'End' in sheet_keys, "begin or end undefined"
    time_list = []
    for _ in sheet['Begin'].keys():
        delta = sheet['End'][_] - sheet['Begin'][_]
        time_list.extend([sheet['Begin'][_]+timedelta(days=i) for i in range(delta.days+1)])
    return time_list

def get_slots(sheet):
    pass

if __name__ == '__main__':
    # book = excel_to_book(f1_in)
    # book_to_calendar(book)
    # aircraft_info = book_to_aircraft_info(book)
    # for _ in aircraft_info:
    #     print(_)

    date = advance_date_now(days=2)

    # print(advance_date_now(days=1, weeks=1, months=1, years=1))
