SHORT DOCUMENTATION

steps:
1) extract task objects with due dates and intervals.
2) compute next expected due date for them, check wether due dates collide, if so compute backwards maintenace opportunities depending on the number of conflicts for a day (if 10 conflicts, compute 10 previous maintenance opportunities for each one).
3) to solve the conflicts, sort by order of priority and keep locking the maintenance opportunities until you are done (solve conflicts one by one). If equal priority just do combinatortial on them. save all the possible assignments and keep a score for all of them, expend the one with least conflicts (best score aswell if greedy)

Maintenance opportunities need to be unique for tasks (or checks) can only have one.

Have a map of maintenance opportunities, fill the map with possible
tasks to assign. (if key no allowed, go one back) you could make copies of these dict for different maintenances. this map could have a to_print very easily.

Have a dict with tasks, each task has a forecasted next due date, intervals, next intervals.

generate conflict tree (dont mess with general schedule), each leaf node is a feasible solution (this is next point I think though). For now, for the conflicts, order the tasks by priority, move tasks one by one solving the conflicts. register backward maintenance opportunities and order them.

tkinter might be nice for visualization (print all or for a certain, step
to another tkinter)