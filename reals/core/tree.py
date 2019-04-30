# A context has all information necessary to generate schedules
# Basically with a Node and a context, we can generate new Nodes
# Each node is an assignment of a schedule

# A schedule assignment is made by concantenating schedules from
# root to leaf node
from treelib import Node, Tree


def tree_branch(calendar, context):

    import ipdb
    ipdb.set_trace()
    pass


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
