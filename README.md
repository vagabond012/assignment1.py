# assignment1.py

Assignment 1 background 
 you are trying to intercept your friend who is on a train loop, while you are travelling on a map of roads. At each minute, your friend moves to the next station in the loop

We are given:
- A directed road network where each road has a cost (in dollars) and a time (in minutes).
- A fixed list of train stations that your friend travels along in a cyclic manner.
- A starting location for yourself and your friend.

Goal is to intercept friend at one of the stations, by arriving at the same time as they do.

Task
write a function intercept(roads, stations, start, friendStart), which computes the cheapest possible cost to intercept your friend at one of the stations they visit, with a tie-breaker on total time.

Basically solution should:
- minimise the toal cost to reach a station
- in the case of ties, favour the path that takes less total time
- Return None if no interception is possible within the contraints


Main function
def intercept(roads, sations, start, friendStart):

Args:
roads: a list of 4 tuples (u, v, cost, time)
staitons: a list of sations IDs in the order your friend vistis them
start: your staring location    
friendStart: the station where freimd starts

Return:
a tuple (totalCost, toalTime, route)
TotalCost: is the total cost of the journey along the optimal valid route. This should be a positive integer.
totalTime is the total time driven of the journey along the optimal valid route. This should be a positive integer.
route is the route you can use to drive from start to the train station you intercept your friend at. This should be a list of integers in the range of 0 to |L| − 1, that represent the locations you travel along the route, ending with the intercepting train station.
or
None if interception is not possible


Comp rquirments
- You must ensure your function runs in O(|R| log |L|) time and O(|L| + |R|) space
- Depending on the severity of the violation, you could lose all or almost all the marks assigned to the question if you violate the complexity.

L is the number of locations (nodes in graph)
R is the number of roads (edges in the graph)
dict and set are not allowed --> therefore can use:
 -list,array 
 -tuples 
 -heapq
 