import numpy

from reals import f1_in, f2_out
from reals.core.parser import excel_to_book, book_to_kwargs_MPO
from reals.core.schedule_classes import FleetManagerBase
from reals.core.tree import Tree


class SchedulerEDF(FleetManagerBase):
    """ Currently for A/C-Checks only, nodes are partial schedules and, tree as total schedules """

    def __init__(self, *args, **kwargs):
        FleetManagerBase.__init__(self, **kwargs)

        self.due_dates = self.fleet.due_dates_from_info(
            self.start_date, self.end_date)

        #a context is a a dictionary with all the next aircraft-due_dates
        # self.context

    @staticmethod
    def schedule_greedy():
        pass

    @staticmethod
    def compute_conflicts(due_dates):
        # conflicts = {}
        # for aircraft in due_dates.keys():
        #     if
        #     self.due_dates[aircraft1]
        pass


if __name__ == '__main__':

    book = excel_to_book(f1_in)
    kwargs = book_to_kwargs_MPO(book)
    scheduler = SchedulerEDF(**kwargs)
    scheduler.fleet.due_dates_from_info(scheduler.calendar.start_date,
                                        scheduler.calendar.end_date)
