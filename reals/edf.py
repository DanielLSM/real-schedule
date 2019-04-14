import numpy
from collections import OrderedDict, defaultdict

from reals import f1_in, f2_out
from reals.core.parser import excel_to_book, book_to_kwargs_MPO
from reals.core.schedule_classes import FleetManagerBase
from reals.core.utils import advance_date, dates_between
from reals.core.tree import Tree

checks = {
    'A_Initial': {
        'initial-days': 'DY-A',
        'initial-hours': 'FH-A',
        'initial-cycles': 'FC-A',
        'max-days': 'ACI-DY',
        'max-hours': 'ACI-FH',
        'max-cycles': 'ACI-FC'
    }
}


class SchedulerEDF(FleetManagerBase):
    """ Currently for A/C-Checks only, nodes are partial schedules and, tree as total schedules """

    def __init__(self, *args, **kwargs):
        FleetManagerBase.__init__(self, **kwargs)
        self.context = self._compute_inital_context()
        # root = Tree()

    # def EDF_heuristic(self,context):
    #     """ The heuristic for EDF is the shortest deadline/due-date """
    #     return list_aircraft_priorities

    def generate_schedules(self, context):
        """ generate schedules using an heuristic, in this case, will only
        generate one by considering one order, in reality, we could generate,
        up to 45!= 1.1962222e+56 XD, but we will generate a single node"""
        schedules = []
        for aircraft in context.keys():
            fill

    def _compute_inital_context(self):
        due_dates = OrderedDict()
        due_dates['A'] = OrderedDict()
        for check in checks.keys():
            for aircraft in self.fleet.aircraft_info.keys():
                DY_i = self.fleet.aircraft_info[aircraft][check][
                    checks[check]['initial-days']]
                FH_i = self.fleet.aircraft_info[aircraft][check][
                    checks[check]['initial-hours']]
                FC_i = self.fleet.aircraft_info[aircraft][check][
                    checks[check]['initial-cycles']]
                maxDY = self.fleet.aircraft_info[aircraft][check][checks[check]
                                                                  ['max-days']]
                maxFH = self.fleet.aircraft_info[aircraft][check][
                    checks[check]['max-hours']]
                maxFC = self.fleet.aircraft_info[aircraft][check][
                    checks[check]['max-cycles']]
                due_dates[aircraft] = self.compute_next_due_date(
                    self.start_date,
                    self.end_date,
                    aircraft,
                    DY_i=DY_i,
                    FH_i=FH_i,
                    FC_i=FC_i,
                    maxDY=maxDY,
                    maxFH=maxFH,
                    maxFC=maxFC)
        return due_dates  #this is the context, e.g, next_due_dates

    def compute_next_due_dates(self,
                               start_due_dates,
                               end_date,
                               check_type='A_Initial'):
        """ Given start_due_dates for all the fleet, and an end_date, assign a schedule
        this is similar to solving a MILP  """
        due_dates = OrderedDict()
        due_dates['A'] = OrderedDict()
        for check in checks.keys():
            maxDY = self.fleet.aircraft_info[aircraft][check][checks[check]
                                                              ['max-days']]
            maxFH = self.fleet.aircraft_info[aircraft][check][checks[check]
                                                              ['max-hours']]
            maxFC = self.fleet.aircraft_info[aircraft][check][checks[check]
                                                              ['max-cycles']]
            for aircraft in start_due_dates.keys():
                due_dates['A'][aircraft] = self.compute_next_due_date(
                    start_due_dates[aircraft],
                    end_date,
                    aircraft,
                    maxDY=maxDY,
                    maxFH=maxFH,
                    maxFC=maxFC)
        return due_dates  #this is the context, e.g, next_due_dates

    def compute_next_due_date(self,
                              start_date,
                              end_date,
                              aircraft,
                              DY_i=0,
                              FH_i=0,
                              FC_i=0,
                              maxDY=0,
                              maxFH=0,
                              maxFC=0):
        DY, FH, FC = DY_i, FH_i, FC_i
        try:
            due_date = advance_date(start_date, DY)
        except:
            import ipdb
            ipdb.set_trace()
        while DY <= maxDY and FH <= maxFH and FC <= maxFC:
            month = start_date.month_name()[0:3]
            DY += 1
            FH += self.fleet.aircraft_info[aircraft]['DFH'][month]
            FC += self.fleet.aircraft_info[aircraft]['DFC'][month]
        due_date = advance_date(due_date, days=int(DY))
        return due_date


if __name__ == '__main__':

    book = excel_to_book(f1_in)
    kwargs = book_to_kwargs_MPO(book)
    scheduler = SchedulerEDF(**kwargs)
