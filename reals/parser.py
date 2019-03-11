import pandas as pd
from reals import f1_in, f2_out
from collections import OrderedDict, defaultdict

# collection of APIs from in and out of python


def excel_to_book(file_input: str):
    book = pd.read_excel(f1_in, sheet_name=None)  # returns an ordered dict
    return book


def to_excel():
    #will save something to an excel eventually
    pass


if __name__ == '__main__':
    try:
        book = excel_to_book(f1_in)
        print(book)
    except e as Exception:
        print(e)
        print('you messed up')
    print("congratulations buddy!!!")