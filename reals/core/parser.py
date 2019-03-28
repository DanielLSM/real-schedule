import pandas as pd
import random
from resources import f1_in, f2_out
from utils import advance_date, advance_date_now

from collections import OrderedDict, defaultdict

# collection of APIs from in and out of python


def excel_to_book(file_input: str):
    try:
        book = pd.read_excel(file_input, sheet_name=None)  # returns an ordered dict
    except Exception as e:
        print(e)
        print('Error parsing the excel file into a dict book buddy!')
    return book

def book_to_kwargs_MPO(book):
    print("INFO: building from xlsx")
    """ given an MPO input, compute dict where keys are aircraft ids and the rest of sheet info is
    organized by aircraft id """
    aircraft_info = get_aircraft_info_MPO(book)
    calendar_restrictions = get_restrictions_MPO(book)

    import ipdb;
    ipdb.set_trace();

    calendar_time_restriction_type = 'day'
    # each type of maintenance as several restrictions we will devide in 2
    # time and hangar restrictions
    m_type_restriction = {'time_type':'day'}
    m_type_restriction['a-type']= {'time':[], 'resources':{extra_slots':{}}
    m_type_restriction['c-type']= {'time':[], 'resources':{extra_slots':{}}
    m_type_restriction['all']= {'time':[]}

    # all these restrictions will restrict the general calendar
    
    print("INFO: information from xlsx parsed with success")
    return {'aircraft_info': aircraft_info, 'restrictions': m_type_restriction}

    # calendar_kwargs = {}
    # start_date = pd.to_datetime(additional['Begin Day'][2017])
    # calendar_kwargs['start_date'] = start_date
    # calendar_kwargs['total_years'] = additional['Total Years'][2017]

    # calendar = Calendar(**calendar_kwargs)

def get_restrictions_MPO(book):

    print('INFO: gathering restrictions info')
    restrictions_info = OrderedDict()
    for sheet_name in book.keys():
        if 'Aircraft ID' not in book[sheet_name].keys():
            for column_idx in book[sheet_name].keys():
                restrictions_info[sheet_name] = book[sheet_name].to_dict()

    print('INFO: restrictions info completed')
    return restrictions_info

def get_aircraft_info_MPO(book):
    print('INFO: gathering aircraft info')
    
    aircraft_info = OrderedDict()    
    for sheet_name in book.keys():
        if 'Aircraft ID' in book[sheet_name].keys():
            #create ordered dict to store aircraft info
            for _ in range(len(book[sheet_name]['Aircraft ID'])):
                a_id = book[sheet_name]['Aircraft ID'][_]
                if a_id not in list(aircraft_info.keys()):
                    aircraft_info[a_id] = OrderedDict()
                if sheet_name not in list(aircraft_info[a_id].keys()):
                    aircraft_info[a_id][sheet_name] = OrderedDict()

            #fill the info of other columns, pandas already adds idx to equal value columns
            for column_idx in book[sheet_name].keys():
                if column_idx != 'Aircraft ID':
                    for _ in range(len(book[sheet_name]['Aircraft ID'])):
                        a_id = book[sheet_name]['Aircraft ID'][_]
                        aircraft_info[a_id][sheet_name][column_idx] = book[sheet_name][column_idx][_]
    
    print('INFO: aircraft info completed')
    return aircraft_info
    

def book_to_tasks(book: dict):
    pass

def to_excel():
    #will save something to an excel eventually
    pass


if __name__ == '__main__':
    try:
        book = excel_to_book(f1_in)
    except Exception as e:
        print('you messed up')
        raise e

    kwargs = book_to_kwargs_MPO(book)









    # book_to_kwargs_MPO(book)
    # print("congratulations buddy!!!")
    # book_to_calendar_kwargs_qichen(book)
