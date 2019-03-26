import pandas as pd
from resources import f1_in, f2_out
from utils import *

from collections import OrderedDict, defaultdict

# collection of APIs from in and out of python


def excel_to_book(file_input: str):
    try:
        import pdb; pdb.set_trace()
        book = pd.read_excel(file_input, sheet_name=None)  # returns an ordered dict
    except Exception as e:
        print(e)
        print('Error parsing the excel file into a dict book buddy!')
    return book




def book_to_calendar_kwargs_qichen(book: dict):
    #currently only C_Checks
    # decompose book into a couple of sheets, use this sheets to restrict
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
    # calendar = Calendar(**calendar_kwargs)

    return calendar_kwargs

def book_to_calendar_kwargs_MPO(book: dict):
    import ipdb; ipdb.set_trace()



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

def to_excel():
    #will save something to an excel eventually
    pass


if __name__ == '__main__':
    try:
        book = excel_to_book(f1_in)
        print(book)
    except Exception as e:
        print('you messed up')
        raise e
    book_to_calendar_kwargs_MPO(book)
    # print("congratulations buddy!!!")
    # book_to_calendar_kwargs_qichen(book)
