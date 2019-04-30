# A context has all information necessary to generate schedules
# Basically with a Node and a context, we can generate new Nodes
# Each node is an assignment of a schedule

# A schedule assignment is made by concantenating schedules from
# root to leaf node
from treelib import Node, Tree


class AircraftNode(Node):
    def __init__(self, aircraft, due_date, waste, last_due_date):
        self.aircraft = aircraft
        self.due_date = due_date
        self.waste = waste
        self.last_due_date = last_due_date


def tree_branch(calendar, context):
    # the idea here is simple, lets schedule the next due dates,
    # but instaead of using milp, lets develop our own tree-search
    # the idea is simple, pick the context, sort by due date
    # start by due dates, expand to the next aircraft
    # if its possible to be greedy, lets be greedy, if not, go one day
    # earlier  and so on, if none of them is possible, backtrack
    # do it until all are scheduled
    # if after exploring everything is filled up, we need to chill
    # on restrictions and add slots, lego.

    #sort by due dates

    #start by the node with shortest due date
    #if backtracks on the root node, we need more slots

    #expand to the next, if possible pick another, if not backtrack
    #do it until there are no nodes left

    variables = list(context.keys())
    schedule_partial
    assigned_variables = {var: 0 for var in variables}
    due_dates = {
        context[aircraft]['A_Initial']['due_date']: aircraft
        for aircraft in variables
    }
    sorted_list = list(due_dates.keys())
    sorted_list.sort()
    variables_order = [due_dates[date] for date in sorted_list]

    new_tree = Tree()
    new_tree.create_node()

    # for var in variables_order:
    def backtrack(var):

        if is_solution():
            return True

        back

    def heuristic_priority(var):
        # chose by next due_date
        pass

    def is_assigned():
        pass

    def is_leaf():
        #if cannot expand, e.g, is solution or is prunned
        #is prunned if it doesnt have more feasible nodes
        pass

    def is_solution():
        for value in assigned_variables.values():
            if not value:
                return False
        return True

    import ipdb
    ipdb.set_trace()
    pass


class BacktrackSchedule:
    def __init__(self, calendar, context):

        # self.schedule_partial =
        self.sol_exist = self._backtrack(calendar, heuristic)
        self.assigned_variables

    def _backtrack():
        pass

    def _is_solution():
        for value in self.assigned_variables.values():
            if not value:
                return False
        return True

    def _unroll_schedule(self):
        #unroll tree until solution and build partial schedule
        return schedule_partial


class ScheduleNode:
    """ A singular node, has connections to a previous node and many next nodes """

    def __init__(self,
                 schedule_assignment,
                 context,
                 name=None,
                 previous_node=None,
                 depth=0):
        self.name = name
        self.schedule_assignment = schedule_assignment
        self.context = context
        self.previous_node = previous_node
        self.children = []
        if previous_node:
            depth = self.previous_node.depth + 1
        self.depth = depth

        def add(self, Node):
            self.next_node.append(Node)


class ScheduleTree:
    """ A tree of N has N layers with M nodes, each node has 2 connections"""

    def __init__(self, context, total_depth=0):
        self.total_depth = total_depth
        self.root = ScheduleNode(schedule_assignment=None,
                                 context=context,
                                 name='root',
                                 depth=0)
