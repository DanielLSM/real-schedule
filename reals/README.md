# Every schedule is composed by assigments of tasks to times

For general purpose usage, times will be called as "opportunities". The objective is to assign tasks before the due dates. A schedule may be seen as a tree. A node therefore, corresponds to the current assignment of tasks.

We need to resolve this conflits one by one. After resolving the conflitcts we can evaluate the outcome of each resolution by exploring greedily in the future, this is monte carlo tree search.

Steps:
1) Lay down first due dates;
2) Resolve conflicts (within the realm of possible oportunities) until there is no problem on first due dates; How to resolve these conflicts? MILP+solver would do. Or rank by priority and go from there, or if equal priority, check, how many opportunities you need, by checking how many tasks you have at the same day.
3) For each of the possible resolutions, do monte carlo tree search to see how good the resolution will be; (this is just average rewards of random actions, basically just go greeedy again, mark due dates exactly on the same future day and check amount of conflicts)
4) Continue to second due date after all first due dates have been scheduled;
5) Proceed until the end of the desired date;
6) Dont forget to rank the solutions by utility, cost lost by doing 
over maintenance (number of days before due date * cost per day per task)
7) How to resolve the local conflicts should be tied to how to solve the global conflicts, the global values should be backpropagated somehow.
8) For the inclusion of RUL i just forsee that it will change the estimated due date by enlarging it. Thus reducing costs.
9) But how exactly to solve the conflicts? This is a very big question.

CHECK HOW MANY CONFLITS THERE ARE IN A CERTAIN DATE, AND CHECK BACKWRODS THE N MORE MAINTENANCE OPPORTUNITIES, USE HEURISTICS AND COMBO THESE ONES, FUTURE VALUE IS TO MAXIMIZED NOT ONLY LOCAL VALUE, LOCAL VALUE 


The occupancy map for the resources will be very imporant when you can have multiple tasks done with the same resource = hangar

https://www.crowdai.org/topics/what-tools-did-you-use/discussion