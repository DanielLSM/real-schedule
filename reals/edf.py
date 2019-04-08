import numpy

from reals import f1_in, f2_out
from reals.core.parser import excel_to_book, book_to_kwargs_MPO
from reals.core.schedule_classes import FleetManagerBase


class SchedulerEDF(FleetManagerBase):
    """ Currently for C-Checks only """

    def __init__(self, *args, **kwargs):
        FleetManagerBase.__init__(self, **kwargs)


if __name__ == '__main__':

    book = excel_to_book(f1_in)
    kwargs = book_to_kwargs_MPO(book)
    scheduler = SchedulerEDF(**kwargs)
    scheduler.fleet.due_dates_from_info(scheduler.calendar.start_date,
                                        scheduler.calendar.end_date)
