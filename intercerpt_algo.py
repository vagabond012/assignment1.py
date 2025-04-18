import heapq

def intercept(roads, stations, start, friendStart):
    """
    Function description:
    Determines the optimal route to intercept a friend riding a train loop at the same time you arrive at a station.
    The goal is to minimise total cost. If multiple routes have the same cost, prefer the one with the least time.

    Approach:
    - Build the graph from the road network as an adjacency list.
    - Use Dijkstra's algorithm to compute minimum cost and time to all locations from the start.
    - Simulate the friend's movement on the train loop, tracking their station at each minute.
    - Identify if and when you can intercept your friend at the same location and time.
    - Return the route that minimises cost (and time if tied), or None if interception is impossible.

    :Input:
    roads: list of tuples (u, v, cost, time)
    stations: list of tuples (station_id, travel_time_to_next_station)
    start: starting location (integer)
    friendStart: starting train station of the friend (integer)

    :Output:
    (min_cost, min_time, route) or None

    :Time complexity:
    O(|R| log |L|), where |R| = number of roads, |L| = number of locations

    :Space complexity:
    O(|L| + |R|)
    """
    graph = [[] for _ in range(1001)]
    for u, v, cost, time in roads:
        graph[u].append((v, cost, time))

    min_cost, min_time, parent = dijkstra(graph, start)
    friend_timeline = simulate_friend(stations, friendStart)
    best = find_best_interception(friend_timeline, min_cost, min_time)

    if best is None:
        return None

    cost, time, station = best
    route = reconstruct_path(parent, station)
    return (cost, time, route)

def dijkstra(graph, start):
    """
    Modified Dijkstra's algorithm using cost as primary and time as tie-breaker.

    :Input:
    graph: adjacency list
    start: starting location

    :Output:
    min_cost: list of minimum costs to all nodes
    min_time: list of minimum times to all nodes
    parent: list of parent pointers for path reconstruction

    :Time complexity:
    O(|R| log |L|)

    :Space complexity:
    O(|L| + |R|)
    """
    INF = float('inf')
    min_cost = [INF] * 1001
    min_time = [INF] * 1001
    parent = [-1] * 1001

    min_cost[start] = 0
    min_time[start] = 0

    heap = [(0, 0, start)]  # (cost, time, location)

    while heap:
        cost, time, u = heapq.heappop(heap)

        if cost > min_cost[u] or (cost == min_cost[u] and time > min_time[u]):
            continue

        for v, edge_cost, edge_time in graph[u]:
            new_cost = cost + edge_cost
            new_time = time + edge_time

            if new_cost < min_cost[v] or (new_cost == min_cost[v] and new_time < min_time[v]):
                min_cost[v] = new_cost
                min_time[v] = new_time
                parent[v] = u
                heapq.heappush(heap, (new_cost, new_time, v))

    return min_cost, min_time, parent

def simulate_friend(stations, friend_start):
    """
    Simulates the friend’s station at each minute based on their travel times.

    :Input:
    stations: list of (station_id, travel_time_to_next_station)
    friend_start: station where friend begins

    :Output:
    A dictionary mapping each minute to the station friend is at then

    :Time complexity:
    O(K), with K up to 1000 (simulated minutes)
    """
    timeline = {}
    idx = next(i for i, (s, _) in enumerate(stations) if s == friend_start)
    time = 0
    while time <= 1000:
        station, travel_time = stations[idx]
        timeline[time] = station
        time += travel_time
        idx = (idx + 1) % len(stations)
    return timeline

def find_best_interception(timeline, min_cost, min_time):
    """
    Finds the best station and time to intercept friend based on cost and time.

    :Input:
    timeline: dictionary mapping time -> station
    min_cost: cost array from Dijkstra
    min_time: time array from Dijkstra

    :Output:
    Tuple of (min_cost, time, station) or None

    :Time complexity:
    O(K), K = 1000
    """
    best = None
    for t, station in timeline.items():
        if min_time[station] == t:
            if best is None or min_cost[station] < best[0] or (min_cost[station] == best[0] and t < best[1]):
                best = (min_cost[station], t, station)
    return best

def reconstruct_path(parent, dest):
    """
    Reconstructs the optimal path to a destination using parent pointers.

    :Input:
    parent: list of parent pointers
    dest: destination node

    :Output:
    Reversed path list from start to dest

    :Time complexity:
    O(P), P = path length
    """
    path = []
    while dest != -1:
        path.append(dest)
        dest = parent[dest]
    return path[::-1]

     